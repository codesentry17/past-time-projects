package com.example.demo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.demo.model.Actor;
import com.example.demo.repository.EmployeeRepository;

import jakarta.transaction.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class EmployeeService {

    @Autowired
    private EmployeeRepository empRep;

    public List<Actor> getAllActors(){
        return empRep.findAll();
    }

    public Optional<Actor> getActorById(int id){

        return empRep.findById(id);
    }

    @Transactional
    public Actor createActor(Actor actor) {
        return empRep.save(actor);
    }

    public String updateActor(int id) {
        return "Actor with ID " + id + " updated";
    }

    public String deleteActor(int id) {
        return "Actor with ID " + id + " deleted";
    }

}
