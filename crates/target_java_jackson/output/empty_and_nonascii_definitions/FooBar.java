// Code generated by jtd-codegen for Java + Jackson v0.2.1

package com.example;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonValue;

public class FooBar {
    @JsonValue
    private String value;

    public FooBar() {
    }

    @JsonCreator
    public FooBar(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
}
