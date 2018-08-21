package com.yabuo.config;

import org.apache.http.HttpHost;

import org.elasticsearch.ElasticsearchException;
import org.elasticsearch.action.admin.indices.create.CreateIndexRequest;
import org.elasticsearch.action.admin.indices.create.CreateIndexResponse;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.beans.factory.config.AbstractFactoryBean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ESConfig extends AbstractFactoryBean<RestHighLevelClient> {
	private static final Logger LOG = LoggerFactory.getLogger(ESConfig.class);

	@Value("${spring.data.elasticsearch.cluster-nodes}")
	private String clusterNodes;
	@Value("${spring.data.elasticsearch.cluster-name}")
	private String clusterName;
	private RestHighLevelClient restHighLevelClient;

	@Override
	public void destroy() {
		try {
			if (restHighLevelClient != null) {
				restHighLevelClient.close();
			}
		} catch (final Exception e) {
			LOG.error("Error closing ElasticSearch client: " , e);
		}
	}

	@Override
	public Class<RestHighLevelClient> getObjectType() {
		return RestHighLevelClient.class;
	}

	@Override
	public boolean isSingleton() {
		return false;
	}

	@Override
	public RestHighLevelClient createInstance() {
		return buildClient();
	}

	private RestHighLevelClient buildClient() {


		try {
			restHighLevelClient = new RestHighLevelClient(
					RestClient.builder(
							new HttpHost("localhost", 9200, "http"),
							new HttpHost("localhost", 9201, "http"))
			);
		}catch(Exception e) {
			LOG.error(e.getMessage());
		}

		try {
			CreateIndexRequest createIndexRequest = new CreateIndexRequest("${elasticsearch.index");
			restHighLevelClient.indices().create(createIndexRequest);
		} catch(java.io.IOException e) {
			e.getLocalizedMessage();
		}

		return restHighLevelClient;
	}
}
