from ursina import *

normals_shader = Shader(language=Shader.GLSL,
                        vertex='''
#version 140
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 transform_matrix;
in vec4 p3d_Vertex;
in vec3 p3d_Normal;
out vec3 world_space_normal;
void main() {
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
    world_space_normal = normalize(transpose( inverse(mat3(transform_matrix)) ) * p3d_Normal.xyz);
}
''',

                        fragment='''
#version 130
uniform vec4 p3d_ColorScale;
in vec2 texcoord;
out vec4 fragColor;
in vec3 world_space_normal;
void main() {
    fragColor = vec4(world_space_normal*0.5+0.5, 1);
    // o_color = float4(l_norm0*0.5+0.5, 1);
    // c.rgb = i.worldNormal*0.5+0.5;
}
''',
                        geometry='',
                        default_input={
                            'transform_matrix': Mat4(),
                        }
                        )
