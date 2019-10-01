package com.example.demo2;

import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.example.demo2.model.Customer;
import com.fasterxml.jackson.core.JsonProcessingException;

@Controller
@RequestMapping(value = "/")
public class GreetingController {

    @RequestMapping(value = "/greeting", method = RequestMethod.GET)
    public ResponseEntity<Customer> greeting(@RequestParam(name="name", required=false, defaultValue="World") String name, Model model)
            throws JsonProcessingException {
//        model.addAttribute("name", name);
        return ResponseEntity.ok(new Customer(name));
    }
}