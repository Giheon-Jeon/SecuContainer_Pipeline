package com.example.hardened;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@SpringBootApplication
@RestController
public class HardenedApplication {

	private static final Logger logger = LoggerFactory.getLogger(HardenedApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(HardenedApplication.class, args);
	}

	@GetMapping("/")
	public String hello() {
		logger.info("Hardened endpoint accessed");
		return "Hello, this is a hardened application!";
	}
}
