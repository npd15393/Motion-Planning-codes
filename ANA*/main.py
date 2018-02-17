import sys
from PIL import Image
import copy
from heap import PQ
import numpy as np
import time

global G ,map_height,map_width, openlist,E,g,e
'''
These variables are determined at runtime and should not be changed or mutated by you
'''
start = (0, 0)  # a single (x,y) tuple, representing the start position of the search algorithm
end = (0, 0)    # a single (x,y) tuple, representing the end position of the search algorithm
difficulty = "trivial" # a string reference to the original import file

'''
These variables determine display coler, and can be changed by you, I guess
'''
NEON_GREEN = (0, 255, 0)
PURPLE = (85, 26, 139)
LIGHT_GRAY = (50, 50, 50)
DARK_GRAY = (100, 100, 100)
'''
These variables are determined and filled algorithmically, and are expected (and required) be mutated by you
'''
path = []       # an ordered list of (x,y) tuples, representing the path to traverse from start-->goal
expanded = {}   # a dictionary of (x,y) tuples, representing nodes that have been expanded
frontier = {}   # a dictionary of (x,y) tuples, representing nodes to expand to in the future
map_width=0
map_height=0

# A heap dict makes argmax operations super fast: O[1]
# Some initializations
openlist = PQ()

G= 10000000
E = [np.inf]
#states = np.full((map.size[1], map.size[0]), np.inf)
g = None

e = None

parents={}


def search(map):
    """
    This function is meant to use the global variables [start, end, path, expanded, frontier] to search through the
    provided map.
    :param map: A '1-concept' PIL PixelAccess object to be searched. (basically a 2d boolean array)
    """

    # O is unoccupied (white); 1 is occupied (black)
    print "pixel value at start point ", map[start[0], start[1]]
    print "pixel value at end point ", map[end[0], end[1]]
    if difficulty== "obcr1.png":
        for i in range(map_width):
            for j in range(map_height):
                map[i,j]=0 if map[i,j]==255 else 1
    # put your final path into this array (so visualize_search can draw it in purple)
    #path.extend([(8,2), (8,3), (8,4), (8,5), (8,6), (8,7)])

    # put your expanded nodes into this dictionary (so visualize_search can draw them in dark gray)
    #expanded.update({(7,2):True, (7,3):True, (7,4):True, (7,5):True, (7,6):True, (7,7):True})

    # put your frontier nodes into this dictionary (so visualize_search can draw them in light gray)
    #frontier.update({(6,2):True, (6,3):True, (6,4):True, (6,5):True, (6,6):True, (6,7):True})

    '''
    YOUR WORK HERE.
    
    I believe in you
        -Gunnar (the TA)-
    '''
    start_time = time.time()
    int_time=start_time
    global st
    st=(start[1],start[0])
    g[st[0],st[1]]=0

    e=(G-g[st[0],st[1]])/heu(st)

    openlist.put(st,e)
    parents[st]=None
    itr_cnt=0

    while not openlist.empty():
        itr_cnt+=1
        improveSoln(map)
        print('Found suboptimal solution ',itr_cnt)
        visualize_search('ana*_so_'+str(itr_cnt)+'.png')
        for n in openlist.elements:
            openlist.delete(n[1])
            if g[n[1][0], n[1][1]]+heu(n[1])<G:
                openlist.put(n[1],-(G-g[n[1][0], n[1][1]])/heu(n[1]))
        print('Suboptimal {0} took {1} seconds'.format (itr_cnt,time.time() - int_time))
        int_time=time.time()

    print('ANA* Search took {0} seconds'.format (time.time() - start_time))
    print('Optimal Path Length {0} using L1 Heuristic'.format(len(path)))

    visualize_search("ana*_optimal_out.png") # see what your search has wrought (and maybe save your results)

def visualize_search(save_file="do_not_save.png"):
    """
    :param save_file: (optional) filename to save image to (no filename given means no save file)
    """
    im = Image.open(difficulty).convert("RGB")
    pixel_access = im.load()

    # draw start and end pixels
    pixel_access[start[0], start[1]] = NEON_GREEN
    pixel_access[end[0], end[1]] = NEON_GREEN


    # draw frontier pixels
    for pixel in frontier.keys():
        pixel_access[pixel[0], pixel[1]] = LIGHT_GRAY

    # draw expanded pixels
    for pixel in expanded.keys():
        pixel_access[pixel[0], pixel[1]] = DARK_GRAY

        # draw path pixels
    for pixel in path:
        pixel_access[pixel[0], pixel[1]] = PURPLE

    # display and (maybe) save results
    im.show()
    if(save_file != "do_not_save.png"):
        im.save(save_file)

    im.close()


def improveSoln(map):
    while not openlist.empty():
        k,s=openlist.get()

        if k<E[len(E)-1]:
            E.append(k)

        if s==end_tr:
            global G
            G=g[s[0],s[1]]
            build_path(s)
            return

        neighbors=[]
        for t in [(s[0]+1,s[1]),(s[0],s[1]+1),(s[0]-1,s[1]),(s[0],s[1]-1)]:
            if t[0]>=0 and t[0]<map_height and t[1]>=0 and t[1]<map_width and map[t[1],t[0]]==0:
                neighbors.append(t)

        for s1 in  neighbors:
            if g[s[0],s[1]]+1<g[s1[0],s1[1]]:
                g[s1[0], s1[1]]=g[s[0],s[1]]+1
                parents[s1]=s
                if g[s1[0], s1[1]]+heu(s1)<G:
                    openlist.delete(s1)
                    openlist.put(s1,-(G-g[s1[0], s1[1]])/heu(s1))
                    frontier.update({(s1[1],s1[0]):True})

        expanded.update({(s[1],s[0]):True})


def build_path(gst):
    while not parents[gst]==None:
        d=[gst[1],gst[0]]
        path.extend([d])
        gst=parents[gst]



# Returns Manhattan disance Heuristic
def heu(pt):
    return abs(pt[0]-end_tr[0])+abs(pt[1]-end_tr[1])+0.0001


if __name__ == "__main__":
    # Throw Errors && Such
    # global difficulty, start, end
    assert sys.version_info[0] == 2                                 # require python 2 (instead of python 3)
    assert len(sys.argv) == 2, "Incorrect Number of arguments"      # require difficulty input

    # Parse input arguments
    function_name = str(sys.argv[0])
    difficulty = str(sys.argv[1])
    print "running " + function_name + " with " + difficulty + " difficulty."

    # Hard code start and end positions of search for each difficulty level
    if difficulty == "trivial.gif":
        start = (8, 1)
        end = (20, 1)
    elif difficulty == "medium.gif":
        start = (8, 201)
        end = (110, 1)
    elif difficulty == "hard.gif":
        start = (10, 1)
        end = (401, 220)
    elif difficulty == "very_hard.gif":
        start = (1, 324)
        end = (580, 1)
    elif difficulty == "obcr1.png":
        start = (112, 476)
        end = (989, 114)
    else:
        assert False, "Incorrect difficulty level provided"

    # Perform search on given image
    im = Image.open(difficulty)
    map_width,map_height=im.size
    g = np.full([map_height, map_width], np.inf)
    e = np.full([map_height, map_width], np.inf)
    global end_tr
    end_tr=(end[1],end[0])
    
    if difficulty== "obcr1.png":
        im=im.convert('1')

    search(im.load())