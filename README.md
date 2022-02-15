# mediapipe_unity

Mediapipe를 이용해서 얼굴의 3D 좌표를 찾고 이를 이용해서 unity에 뿌려주는 mesh파일 만들기
Mesh를 만들기 위해서 좌표, 삼각형 관계, uv 좌표, 이미지
Mediapipe는 총 468개의 3D 좌표를 제공합니다
삼각형(Triangles)가 필요한데 이는 문서상에는 주어지지 않고 샘플로 주는 fbx 파일에 있어서 저는 따로 추출해서 사용하였습니다
그 결과는 traigle_ver1.txt에 적혀져 있습니다
본 코드에서는 카메라 영상에 대해서 3d vertex들을 저장(face_vertex.txt)하고 이에 맞는 uv 좌표(mtl_vertex.txt)에 저장하였습니다.
이렇게 한 이유는 저는  unity 코드상에서 따로 파싱을해서 mesh로 뿌려주는 방식으로 사용하고 있습니다
 

1. find face vertex using mediapipe
2. rendering it using unity
3. 3DMM Face Model
 - https://www.face-rec.org/algorithms/3d_morph/morphmod2.pdf
  


