package com.example.demo;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication implements CommandLineRunner {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	@Override
	public void run(String... args) {
		int index = 13, sum = 0, K = 0;

		while (K < index) {
			K = K + 1;
			sum = sum + K;
		}

		System.out.println("Value: " + sum);
	}
}
