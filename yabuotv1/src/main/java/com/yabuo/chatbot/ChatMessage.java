package com.yabuo.chatbot;

import org.springframework.data.annotation.Id;
import org.springframework.data.elasticsearch.annotations.Document;

@Document(indexName = "yabuo", type = "chatMessage")
public class ChatMessage {

	@Id
	private int id;
	private String phrase;

	public ChatMessage() {
	}

	public ChatMessage(int id, String phrase) {
		this.id = id;
		this.phrase = phrase;
	}

	public int getId() {
		return this.id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getPhrase() {
		return this.phrase;
	}

	public void setPhrase(String phrase) {
		this.phrase = phrase;
	}

	@Override
	public String toString() {
		return "ChatMessage[" +
				"id='" + id + '\'' +
				", phrase='" + phrase + '\'' +
				']';
	}

}
