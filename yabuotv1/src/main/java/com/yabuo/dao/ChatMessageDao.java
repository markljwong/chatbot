package com.yabuo.dao;

import com.yabuo.model.ChatMessage;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import org.elasticsearch.ElasticsearchException;
import org.elasticsearch.action.delete.DeleteRequest;
import org.elasticsearch.action.delete.DeleteResponse;
import org.elasticsearch.action.get.GetRequest;
import org.elasticsearch.action.get.GetResponse;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.action.update.UpdateRequest;
import org.elasticsearch.action.update.UpdateResponse;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.common.xcontent.XContentType;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@Repository
public class ChatMessageDao {
	private final String INDEX = "$[elasticsearch.index}";
	private final String TYPE = "${elasticsearch.type}";
	private RestHighLevelClient restHighLevelClient;
	private ObjectMapper objectMapper;

	@Autowired
	public ChatMessageDao(ObjectMapper objectMapper, RestHighLevelClient restHighLevelClient) {
		this.objectMapper = objectMapper;
		this.restHighLevelClient = restHighLevelClient;
	}

	public ChatMessage insertChatMessage(ChatMessage chatMessage) {
		chatMessage.setId(UUID.randomUUID().toString());
		Map<String, Object> dataMap = objectMapper.convertValue(chatMessage, Map.class);
		IndexRequest indexRequest = new IndexRequest(INDEX, TYPE, chatMessage.getId())
				.source(dataMap);

		try {
			IndexResponse response = restHighLevelClient.index(indexRequest);
		} catch(ElasticsearchException e) {
			e.getDetailedMessage();
		} catch(java.io.IOException e) {
			e.getLocalizedMessage();
		}

		return chatMessage;
	}

	public Map<String, Object> getChatMessageById(String id) {
		GetRequest getRequest = new GetRequest(INDEX, TYPE, id);
		System.out.println(TYPE);
		System.out.println(id);
		GetResponse getResponse = null;

		try {
			getResponse = restHighLevelClient.get(getRequest);
		} catch (java.io.IOException e) {
			e.getLocalizedMessage();
		}

		Map<String, Object> sourceAsMap = getResponse.getSourceAsMap();
		return sourceAsMap;
	}

	public Map<String, Object> updateChatMessageById(String id, ChatMessage chatMessage) {
		UpdateRequest updateRequest = new UpdateRequest(INDEX, TYPE, id)
				.fetchSource(true);
		Map<String, Object> error = new HashMap<>();
		error.put("Error", "Unable to update Chat Message");

		try {
			String chatMessageJson = objectMapper.writeValueAsString(chatMessage);
			updateRequest.doc(chatMessageJson, XContentType.JSON);
			UpdateResponse updateResponse = restHighLevelClient.update(updateRequest);
			Map<String, Object> sourceAsMap = updateResponse.getGetResult().sourceAsMap();
			return sourceAsMap;
		}catch (JsonProcessingException e){
			e.getMessage();
		} catch (java.io.IOException e){
			e.getLocalizedMessage();
		}

		return error;
	}

	public void deleteChatMessageById(String id) {
		DeleteRequest deleteRequest = new DeleteRequest(INDEX, TYPE, id);
		try {
			DeleteResponse deleteResponse = restHighLevelClient.delete(deleteRequest);
		} catch (java.io.IOException e){
			e.getLocalizedMessage();
		}
	}
}
