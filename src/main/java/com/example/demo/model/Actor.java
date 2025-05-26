package com.example.demo.model;

import java.time.LocalDateTime;

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

    @Column(name = "last_update", nullable = false)
    private LocalDateTime lastUpdate;

    public int getId(){
        return this.id;
    }

    public String getFirstName(){
        return this.firstName;
    }

    public String getLastName(){
        return this.lastName;
    }

    public LocalDateTime getLastUpdate(){
        return this.lastUpdate;
    }

    @Override
    public int compareTo(Actor other) {
        return this.firstName.compareTo(other.getFirstName());
    }

}
