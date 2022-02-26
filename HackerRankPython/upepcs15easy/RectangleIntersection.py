
import sys

class RectangeIntersection():    
    def __init__(self):
        pass

    def process(self):
        count = 0
        data = {}
        line = "."

        try:
            while line != "":
                ar = list(map(float, input().strip().split(' ')))
                data[count] = ar        
                count += 1
        except EOFError:
            None

        for i in range(0, len(data)):
            for j in range(i + 1, len(data)):
                
                i_xc = data[i][0]
                i_yc = data[i][1]
                i_width = data[i][2]
                i_height = data[i][3]

                j_xc = data[j][0]
                j_yc = data[j][1]
                j_width = data[j][2]
                j_height = data[j][3]

                ix = i_xc - (i_width / 2)
                iy = i_yc - (i_height / 2)
                ix2 = i_xc + (i_width / 2)
                iy2 = i_yc + (i_height / 2)

                jx = j_xc - (j_width / 2)
                jy = j_yc - (j_height / 2)
                jx2 = j_xc + (j_width / 2)
                jy2 = j_yc + (j_height / 2)
                
                if (
                        ((jx >= ix and jx <= ix2) or
                        (ix >= jx and ix <= jx2))

                    and
                        ((jy >= iy and jy <= iy2) or
                        (iy >= jy and iy <= jy2))
                    ):
                    print(f"Rectangle {i} intersects with Rectangle {j}")


    def __del__(self):
        pass
