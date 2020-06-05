from ursina import *
from panda3d.core import Shader as Panda3dShader

# basic_lighting_shader = Panda3dShader.make(Panda3dShader.SL_GLSL,
basic_lighting_shader = Shader(
    vertex='''
#version 130
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 transform_matrix;
in vec4 p3d_Vertex;
in vec2 p3d_MultiTexCoord0;
in vec3 p3d_Normal;
out vec2 texcoord;
out vec3 world_space_normal;
void main() {
  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
  texcoord = p3d_MultiTexCoord0;
  vec4 invcamx = transform_matrix[0];
  vec4 invcamy = transform_matrix[1];
  vec4 invcamz = transform_matrix[2];
  vec4 invcamw = transform_matrix[3];
  mat3 invcam = mat3(
                          invcamx[0], invcamx[1], invcamx[2],
                          invcamy[0], invcamy[1], invcamy[2],
                          invcamz[0], invcamz[1], invcamz[2]
                      );
  world_space_normal = normalize(p3d_Normal * invcam);
}
''',

    fragment='''
#version 130
uniform sampler2D p3d_Texture0;
uniform vec4 p3d_ColorScale;
in vec2 texcoord;
in vec3 world_space_normal;
uniform vec4 top_color;
uniform vec4 bottom_color;
uniform vec4 left_color;
uniform vec4 right_color;
uniform vec4 front_color;
uniform vec4 back_color;
out vec4 fragColor;
void main() {
    vec4 norm = vec4(world_space_normal*0.5+0.5, 1);
    // float grey = 0.21 * norm.r + 0.71 * norm.g + 0.07 * norm.b;
    // norm = vec4(grey, grey, grey, 1);
    vec4 color = texture(p3d_Texture0, texcoord) * p3d_ColorScale;
    // vec4 color = vec4(0.0, 0.0, 0.0, 0.0);
    float normal_y = world_space_normal.y + .5;
    color += mix(bottom_color, top_color, norm.z) / 3.;
    color += mix(right_color, left_color, norm.x) / 3.;
    color += mix(front_color, back_color, norm.y) / 3.;
    fragColor = vec4(color.rgb, 1);
}
''',
    geometry='',
    default_input={
        'transform_matrix': Mat4(),
        'top_color': color.red,
        'bottom_color': color.green,
        'left_color': color.black,
        'right_color': color.black,
        'front_color': color.black,
        'back_color': color.black,
    }
)
