package com.example.demo.model;

import java.time.LocalDateTime;

import org.hibernate.annotations.Generated;
import org.hibernate.generator.EventType;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "actor")
public class Actor implements Comparable<Actor>{

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "actor_id")
    private int id;

    @Column(name = "first_name", nullable = false, length = 45)
    private String firstName;
    
    @Column(name = "last_name", nullable = false, length = 45)
    private String lastName;
    
    @Column(name = "last_update", insertable = false, updatable = false)
    @Generated(event = EventType.INSERT)
    private LocalDateTime lastUpdate;
    
    /**
     * @return this is for Hibernate's working
     */
    public Actor() {}

    /**
     * @param firstName
     * @param lastName
     * @return for POST 
     */
    public Actor(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    /**
     * 
     * @param id
     * @param firstName
     * @param lastName
     * @return for PUT
     */
    public Actor(int id, String firstName, String lastName) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public int getId(){
        return this.id;
    }
    
    public String getFirstName(){
        return this.firstName;
    }
    
    public String getLastName(){
        return this.lastName;
    }
    
    public LocalDateTime getLastUpdate() {
        return lastUpdate;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setLastUpdate(LocalDateTime lastUpdate) {
        this.lastUpdate = lastUpdate;
    }
  

    @Override
    public int compareTo(Actor other) {
        return this.firstName.compareTo(other.getFirstName());
    }

    // public Actor(String firstName, String lastName) {
    //     this.firstName = firstName;
    //     this.lastName = lastName;
    // }

}
