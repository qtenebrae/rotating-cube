# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2023-11-07

### Added

- Module `VoxelEngine`, is an engine for working with voxel objects in a graphical application.
    - `on_init`, called when VoxelEngine is initialised and creates the necessary objects, such as Textures, Player,
      ShaderProgram and Scene.
    - `update`, updates the state of game objects, ShaderProgram and Scene.
    - `render`, clears the screen, draws the scene, and updates the display.
    - `handle_events`, handles Pygame events such as keystrokes or exiting the application.
    - `run`, starts the main application loop, handles events, updates and draws the scene while the application is
      running.
- Module `Camera`, represents the camera in the 3D scene and is responsible for controlling its position and direction.
    - `update`, updates the direction vectors and the camera view matrix.
    - `update_view_matrix`, updates the camera view matrix based on the current position and direction.
    - `update_vectors`, updates camera direction vectors based on current rotation angles.
    - `rotate_pitch`, rotates the camera vertically by a specified angle.
    - `rotate_yaw`, rotates the camera horizontally by a specified angle.
- Module `Player`, represents the player in the game environment and is responsible for first-person control of the game
  character.
    - `update`, updates the player's state by controlling with keyboard and mouse.
    - `mouse_control`, handles player control with the mouse.
    - `keyboard_control`, handles player control using the keyboard.
- Module `Scene`, is responsible for controlling and displaying the objects that are in this scene.
    - `update`, updates the state of the scene.
    - `render`, sketching the scene.
- Module `ShaderProgram`, represents a shader programme in a graphics application.
    - `set_uniforms_on_init`, sets the values of the uniform variables of the shader program at initialisation.
    - `update`, updates the values of the uniform variables of the shader program.
    - `get_program`, loads and compiles shader programs from vertex and fragment shader files.
- Module `Textures`, is responsible for managing textures in the graphical environment used in an application or game.
    - `load`, loads a texture from a file and performs the necessary operations to prepare it for use.
- Module `BaseMesh`, is the base class for other grid classes.
    - `get_vertex_data`, returns the vertex data
    - `get_vao`, returns a Vertex Array Object (VAO).
    - `render`, draws the object.
    - `update`, updates the state of the object.
- Module `BlockMesh`, represents the block grid in the 3D scene and is responsible for creating and drawing vertex data
  of the block.
    - `get_vertex_data`, returns the vertex data for the block.
- Vertex shaders program `block.vert`, is used to transform the vertices of the models.
- Fragment shaders program `block.frag`, determine the final colour of each slice, and can use information from vertex
  shaders and other data to apply lighting, texturing, effects or other operations.