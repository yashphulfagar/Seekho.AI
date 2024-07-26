import textwrap
import numpy as np
import pandas as pd
import google.generativeai as genai
from IPython.display import Markdown
API_KEY=userdata.get('API_KEY')
genai.configure(api_key=API_KEY)