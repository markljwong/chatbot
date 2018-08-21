package com.yabuo.chatbot;

import org.elasticsearch.client.Client;
import org.elasticsearch.client.transport.TransportClient;
import org.elasticsearch.common.settings.Settings;
import org.elasticsearch.common.transport.InetSocketTransportAddress;

import org.elasticsearch.transport.Transport;
import org.elasticsearch.transport.client.PreBuiltTransportClient;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.data.elasticsearch.core.ElasticsearchTemplate;
import org.springframework.data.elasticsearch.repository.config.EnableElasticsearchRepositories;

import java.net.InetAddress;
import java.net.UnknownHostException;

@Configuration
@EnableElasticsearchRepositories(basePackages = "com.yabuo.chatbot.repository")
@ComponentScan(basePackages = "com.yabuo.chatbot.service")
public class Config {
	@Value("${elasticsearch.home:/elasticsearch/ES6.3.2}")
	private String esHome;

	@Value("${elasticsearch.cluster.name:es}")
	private int clusterName;

	@Value("${elasticsearch.clustername}")
	private String esClusterName;

	@Bean
	public Client client() {
		TransportClient client = null;
		try {
			final Settings esSetttings = Settings.builder()
					.put("client.transport.sniff", true)
					.put("path.home", esHome)
					.put("cluster.name", clusterName).build();
			client = new PreBuiltTransportClient(esSetttings);
			client.addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("127.0.0.1"), 9300));
		} catch (UnknownHostException e) {
			e.printStackTrace();
		}
		return client;
	}

	@Bean
	public ElasticsearchOperations esTemplate() {
		return new ElasticsearchTemplate(client());
	}
}
