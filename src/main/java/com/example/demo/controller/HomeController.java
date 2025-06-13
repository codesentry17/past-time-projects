package com.example.demo.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import com.example.demo.service.EmployeeService;
import com.example.demo.dto.ActorDTO;
import com.example.demo.model.Actor;

import java.net.URI;
import java.util.List;
import java.util.Optional;
import java.util.Map;

import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PutMapping;

/*
 * Ideally, we should use DTOs for getting and sending payload, and not using Entity objects in Controller layer. 
 */


@RestController
@RequestMapping("/")
public class HomeController {

    /*
     *  return ResponseEntity.ok(cart);                          // 200
     *  return ResponseEntity.created(uri).body(cart);           // 201
     *  return ResponseEntity.notFound().build();                // 404
     *  return ResponseEntity.badRequest().body(errorMessage);   // 400
    */ 

    /*
     * Concept error, sending id (actor_id in db) as as payload which is wrong.
     */

    @Autowired
    private EmployeeService empSer;

    @GetMapping
    public ResponseEntity<List<Actor>> getAllActors(){
        return ResponseEntity.ok(empSer.getAllActors());
    }

    @GetMapping("/{id}")
    public ResponseEntity<Actor> getActorById(@PathVariable int id){
        
        Optional<Actor> actor = empSer.getActorById(id);

        if(actor.isPresent()){
            return ResponseEntity.ok(actor.get());
        }else{
            return ResponseEntity.notFound().build();
        }
    }

    @PostMapping
    public ResponseEntity<?> createActor(@RequestBody ActorDTO actor) {
        
        Actor newActor = empSer.createActor(actor);

        // build URI for created object location
        URI uri = ServletUriComponentsBuilder
                .fromCurrentRequest()
                .path("/{id}")
                .buildAndExpand(newActor.getId())
                .toUri();

        
        return ResponseEntity.created(uri).body(newActor);
    }


    @PutMapping("/{id}")
    public ResponseEntity<?> updateActor(
        @PathVariable int id, 
        @RequestBody ActorDTO actor) {
        
        Actor updatedActor = empSer.updateActor(id, actor);

        return ResponseEntity.ok().body(updatedActor);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteActor(@PathVariable int id) {

        empSer.deleteActor(id);
        return ResponseEntity.noContent().build();
    }
    

}