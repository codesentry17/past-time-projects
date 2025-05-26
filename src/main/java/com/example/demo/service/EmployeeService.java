package com.example.demo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.demo.model.Actor;
import com.example.demo.repository.EmployeeRepository;

import java.util.List;

@Service
public class EmployeeService {

    @Autowired
    private EmployeeRepository empRep;

    public List<Actor> getAllActors(){
        return empRep.findAll();
    }

    public String getActorById(int id){
        return "Sending data of Actor with id "+id;
    }

    public String createActor() {
        return "Actor created";
    }

    public String updateActor(int id) {
        return "Actor with ID " + id + " updated";
    }

    public String deleteActor(int id) {
        return "Actor with ID " + id + " deleted";
    }

}
