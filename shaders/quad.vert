// This file is not relevant in this version of the project, but can be used at a later date

#version 330 core

layout (location = 0) in vec3 in_position;
layout (location = 1) in vec3 in_color;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

out vec3 color;

void main() {
    color = in_color;
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}