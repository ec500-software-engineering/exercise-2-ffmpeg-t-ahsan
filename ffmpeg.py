import queue
import threading
import os
import compute
vids_path = './videos'
out = './processed'

def main():
	q = queue.Queue()
	folder = os.listdir(vids_path)
	for file in folder:
		q.put(vids_path+"/"+file)
	for i in range(2):
		worker = threading.Thread(target=compute.process, args=(q,vids_path))
		worker.start()

if __name__ == "__main__":
	main()
