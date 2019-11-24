#tmpmain.py
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent / 'solver'))

from GUI import main
if __name__ == '__main__':
    main()
