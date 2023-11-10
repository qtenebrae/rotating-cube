#version 330 core

layout (location = 0) in vec3 in_position;

uniform mat4 m_proj;
uniform mat4 m_view;
uniform mat4 m_model;

out vec2 uv;
flat out int selected_texture;

const vec2 uv_coords[4] = vec2[4](
vec2(0, 0), vec2(0, 1),
vec2(1, 0), vec2(1, 1)
);

const int uv_indices[12] = int[12](
1, 0, 2, 1, 2, 3,
3, 0, 2, 3, 1, 0
);

void main() {
    // Вычисление индекса UV-координаты для текущего вертекса
    int uv_index = gl_VertexID % 6;
    // Получение UV-координаты из предопределенного массива
    uv = uv_coords[uv_indices[uv_index]];
    // Определение выбранной текстуры на основе индекса вертекса
    if (gl_VertexID / 6 == 0) {
        selected_texture = 0;
    } else if (gl_VertexID / 6 == 1) {
        selected_texture = 1;
    } else if (gl_VertexID / 6 == 2) {
        selected_texture = 2;
    } else if (gl_VertexID / 6 == 3) {
        selected_texture = 3;
    } else if (gl_VertexID / 6 == 4) {
        selected_texture = 4;
    } else if (gl_VertexID / 6 == 5) {
        selected_texture = 5;
    }

    // Вычисление позиции вертекса в пространстве
    gl_Position = m_proj * m_view * m_model * vec4(in_position, 1.0);
}