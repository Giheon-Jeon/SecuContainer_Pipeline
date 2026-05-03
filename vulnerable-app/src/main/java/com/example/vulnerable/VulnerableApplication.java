package com.example.vulnerable;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

@SpringBootApplication
@RestController
public class VulnerableApplication {

	private static final Logger logger = LogManager.getLogger(VulnerableApplication.class);

	public static void main(String[] args) {
		SpringApplication.run(VulnerableApplication.class, args);
	}

	@GetMapping("/")
	public String hello() {
		logger.info("Vulnerable endpoint accessed");
		return "Hello, this is a vulnerable application!";
	}
}
