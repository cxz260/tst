{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9760a3d6",
   "metadata": {
    "_cell_guid": "e7f25665-1dbf-46f2-996c-45c644655c1b",
    "_uuid": "6727c81a-3b15-4614-8290-1d3b7e4d2f50",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-08-05T18:10:46.520425Z",
     "iopub.status.busy": "2022-08-05T18:10:46.519579Z",
     "iopub.status.idle": "2022-08-05T18:10:46.550259Z",
     "shell.execute_reply": "2022-08-05T18:10:46.548876Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.039269,
     "end_time": "2022-08-05T18:10:46.553416",
     "exception": false,
     "start_time": "2022-08-05T18:10:46.514147",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-08-05 18:10:46,536 : DEBUG : __main__ : A debug message\n",
      "2022-08-05 18:10:46,540 : INFO : __main__ : An info message\n",
      "2022-08-05 18:10:46,542 : WARNING : __main__ : Something is not right.\n",
      "2022-08-05 18:10:46,543 : ERROR : __main__ : A Major error has happened.\n",
      "2022-08-05 18:10:46,545 : CRITICAL : __main__ : Fatal error. Cannot continue\n"
     ]
    }
   ],
   "source": [
    "import logging\n",
    "\n",
    "# Gets or creates a logger\n",
    "logger = logging.getLogger(__name__)  \n",
    "\n",
    "# set log level\n",
    "logger.setLevel(logging.DEBUG)\n",
    "\n",
    "# define file handler and set formatterpwd\n",
    "\n",
    "file_handler = logging.FileHandler('logfile.log')\n",
    "formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')\n",
    "file_handler.setFormatter(formatter)\n",
    "file_handler.setLevel(logging.DEBUG)\n",
    "# add file handler to logger\n",
    "logger.addHandler(file_handler)\n",
    "\n",
    "# add console log\n",
    "con_handler = logging.StreamHandler()\n",
    "con_handler.setFormatter(formatter)\n",
    "logger.addHandler(con_handler)\n",
    "\n",
    "# Logs\n",
    "logger.debug('A debug message')\n",
    "logger.info('An info message')\n",
    "logger.warning('Something is not right.')\n",
    "logger.error('A Major error has happened.')\n",
    "logger.critical('Fatal error. Cannot continue')# This Python 3 environment comes with many helpful analytics libraries installed\n",
    "# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python\n",
    "# For example, here's several helpful packages to load\n",
    "\n",
    "import numpy as np # linear algebra\n",
    "import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)\n",
    "import sys\n",
    "\n",
    "# Input data files are available in the read-only \"../input/\" directory\n",
    "# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory\n",
    "\n",
    "import os\n",
    "for dirname, _, filenames in os.walk('/kaggle/input'):\n",
    "    for filename in filenames:\n",
    "        print(os.path.join(dirname, filename))\n",
    "\n",
    "# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using \"Save & Run All\" \n",
    "# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 9.965279,
   "end_time": "2022-08-05T18:10:47.177561",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-08-05T18:10:37.212282",
   "version": "2.3.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
