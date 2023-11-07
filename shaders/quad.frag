// This file is not relevant in this version of the project, but can be used at a later date

#version 330 core

layout (location = 0) out vec4 fragColor;

in vec3 color;


void main() {
    fragColor = vec4(color, 1.0);
}