package com.yabuo.chatbot;

import static org.junit.Assert.assertEquals;

import java.io.IOException;
import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;
import java.util.stream.Collectors;

import org.elasticsearch.action.DocWriteResponse.Result;
import org.elasticsearch.action.delete.DeleteResponse;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.action.search.SearchType;
import org.elasticsearch.client.Client;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;
import org.elasticsearch.common.xcontent.XContentBuilder;
import org.elasticsearch.common.xcontent.XContentFactory;
import org.elasticsearch.common.xcontent.XContentType;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.transport.client.PreBuiltTransportClient;
import org.junit.Before;
import org.junit.Test;

import com.alibaba.fastjson.JSON;

import com.yabuo.chatbot.ChatMessage;

public class ESManualTest {
	private List<ChatMessage> listOfPersons = new ArrayList<>();
	private Client client = null;

	@Before
	public void setUp() throws UnknownHostException {
		ChatMessage msg1 = new ChatMessage(10, "World Hello");
		ChatMessage msg2 = new ChatMessage(25, "Yabuo Hello");
		listOfPersons.add(msg1);
		listOfPersons.add(msg2);

		client = new PreBuiltTransportClient(Settings.builder().put("client.transport.sniff", true)
				.put("cluster.name","elasticsearch").build())
				.addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("127.0.0.1"), 9300));
	}

	@Test
	public void givenJsonString_whenJavaObject_thenIndexDocument() {
		String jsonObject = "{\"id\":10,\"phrase\":\"Hello\"}";
		IndexResponse response = client
				.prepareIndex("yabuo", "Hello")
				.setSource(jsonObject, XContentType.JSON)
				.get();
		String index = response.getIndex();
		String type = response.getType();

		assertEquals(Result.CREATED, response.getResult());
		assertEquals(index, "yabuo");
		assertEquals(type, "Hello");
	}

	@Test
	public void givenDocumentId_whenJavaObject_thenDeleteDocument() {
		String jsonObject = "{\"id\":10,\"phrase\":\"Hello\"}";
		IndexResponse response = client
				.prepareIndex("yabuo", "Doe")
				.setSource(jsonObject, XContentType.JSON)
				.get();
		String id = response.getId();
		DeleteResponse deleteResponse = client
				.prepareDelete("yabuo", "Hello", id)
				.get();

		assertEquals(Result.DELETED,deleteResponse.getResult());
	}

	@Test
	public void givenSearchRequest_whenMatchAll_thenReturnAllResults() {
		SearchResponse response = client
				.prepareSearch()
				.execute()
				.actionGet();
		SearchHit[] searchHits = response
				.getHits()
				.getHits();
		List<ChatMessage> results = Arrays.stream(searchHits)
				.map(hit -> JSON.parseObject(hit.getSourceAsString(), ChatMessage.class))
				.collect(Collectors.toList());
	}

	@Test
	public void givenSearchParameters_thenReturnResults() {
		SearchResponse response = client
				.prepareSearch()
				.setTypes()
				.setSearchType(SearchType.DFS_QUERY_THEN_FETCH)
				.setPostFilter(QueryBuilders
						.rangeQuery("age")
						.from(5)
						.to(15))
				.setFrom(0)
				.setSize(60)
				.setExplain(true)
				.execute()
				.actionGet();

		SearchResponse response2 = client
				.prepareSearch()
				.setTypes()
				.setSearchType(SearchType.DFS_QUERY_THEN_FETCH)
				.setPostFilter(QueryBuilders.simpleQueryStringQuery("+World -Hello OR Yabuo"))
				.setFrom(0)
				.setSize(60)
				.setExplain(true)
				.execute()
				.actionGet();

		SearchResponse response3 = client
				.prepareSearch()
				.setTypes()
				.setSearchType(SearchType.DFS_QUERY_THEN_FETCH)
				.setPostFilter(QueryBuilders.matchQuery("Yabuo", "Phrase*"))
				.setFrom(0)
				.setSize(60)
				.setExplain(true)
				.execute()
				.actionGet();
		response2.getHits();
		response3.getHits();

		final List<ChatMessage> results = Arrays.stream(response.getHits().getHits())
				.map(hit -> JSON.parseObject(hit.getSourceAsString(), ChatMessage.class))
				.collect(Collectors.toList());
	}

	@Test
	public void givenContentBuilder_whenHelpers_thanIndexJson() throws IOException {
		XContentBuilder builder = XContentFactory
				.jsonBuilder()
				.startObject()
				.field("fullName", "Test")
				.field("salary", "11500")
				.field("age", "10")
				.endObject();
		IndexResponse response = client
				.prepareIndex("people", "Doe")
				.setSource(builder)
				.get();

		assertEquals(Result.CREATED, response.getResult());
	}
}
