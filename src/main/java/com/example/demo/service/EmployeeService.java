package com.example.demo.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.dto.ActorDTO;
import com.example.demo.model.Actor;
import com.example.demo.repository.EmployeeRepository;

import jakarta.transaction.Transactional;

import java.lang.foreign.Linker.Option;
import java.util.List;
import java.util.Optional;

@Service
@Transactional
public class EmployeeService {

    @Autowired
    private EmployeeRepository empRep;

    public List<Actor> getAllActors(){
        return empRep.findAll();
    }

    public Optional<Actor> getActorById(int id){

        return empRep.findById(id);
    }

    public Actor createActor(ActorDTO actor) {

        return empRep.save(new Actor(
            actor.firstName(), 
            actor.lastName())
        );
    }

    public Actor updateActor(int id, ActorDTO actor) {

        return empRep.save(new Actor(
                id, 
                actor.firstName(), 
                actor.lastName())
            );
    }

    public void deleteActor(int id) {
    
        Optional<Actor> actor = empRep.findById(id);

        if(actor.isPresent())
            empRep.delete(actor.get());
    
    }

}
