package com.example.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.service.EmployeeService;
import com.example.demo.model.Actor;

import java.util.List;

@RestController
@RequestMapping("/")
public class HomeController {

    @Autowired
    private EmployeeService empSer;

    @GetMapping
    public List<Actor> getAllActors(){
        return empSer.getAllActors();
    }

    @GetMapping("/{id}")
    public String getActorById(@PathVariable int id){
        return empSer.getActorById(id);
    }

}