#version 330 core

layout (location = 0) out vec4 fragColor;

uniform sampler2D u_textures[6];

in vec2 uv;
flat in int selected_texture;

void main() {
    // Получение цвета пикселя из выбранной текстуры используя UV-координаты
    vec3 tex_col = texture(u_textures[selected_texture], uv).rgb;
    // Установка цвета фрагмента
    fragColor = vec4(tex_col, 1);
}