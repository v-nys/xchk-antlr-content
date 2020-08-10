from xchk_core import contentviews as basecv
from xchk_core.courses import Course
from .contentviews import *

course = Course('antlr',
                'ANTLR',
                [(DemoANTLRView,[])],
                "git@github.com:v-nys/xchk-antlr-model-solutions.git")
