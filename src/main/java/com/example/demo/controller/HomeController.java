package com.example.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.example.demo.service.EmployeeService;
import com.example.demo.model.Actor;

import java.net.URI;
import java.util.List;
import java.util.Optional;

import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;



@RestController
@RequestMapping("/")
public class HomeController {

    /*
        return ResponseEntity.ok(cart);                          // 200
        return ResponseEntity.created(uri).body(cart);           // 201
        return ResponseEntity.notFound().build();                // 404
        return ResponseEntity.badRequest().body(errorMessage);   // 400
    */ 

    @Autowired
    private EmployeeService empSer;

    @GetMapping
    public ResponseEntity<List<Actor>> getAllActors(){
        return ResponseEntity.ok(empSer.getAllActors());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Actor> getActorById(@PathVariable int id){
        
        Optional<Actor> response = empSer.getActorById(id);

        if(response.isPresent()){
            return ResponseEntity.ok(response.get());
        }else{
            return ResponseEntity.notFound().build();
        }
    }

    @PostMapping
    public ResponseEntity<Actor> createActor(@RequestBody Actor actor) {
        
        Actor newActor = empSer.createActor(actor);

        // build URI for created object location
        URI uri = ServletUriComponentsBuilder
                .fromCurrentRequest()
                .path("/{id}")
                .buildAndExpand(newActor.getId())
                .toUri();

        
        return ResponseEntity.created(uri).body(newActor);
    }


    

}