import tkinter as tk
from time import time, sleep

root = tk.Tk()

config = {"amount": tk.IntVar()}

tk.Label(root, text = "Polygon Performance", font = ("Arial", 16, "bold")).pack(padx = 10)
tk.Scale(root, variable = config["amount"], from_ = 0, to_ = 1000, length = 1000, orient = "horizontal").pack(padx = 10)

canvas = tk.Canvas(
	root,
	height = 600,
	bg = "black",
	highlightthickness = 0
)
canvas.pack(fill = "both", expand = True, padx = 10, pady = 10)

def update():
	start = time()

	canvas.delete("all")

	for i in range(config["amount"].get()):
		canvas.create_polygon(
			25 + (i%40)*30, 0  + (i//40)*30,
			50 + (i%40)*30, 20 + (i//40)*30,
			40 + (i%40)*30, 50 + (i//40)*30,
			10 + (i%40)*30, 50 + (i//40)*30,
			0  + (i%40)*30, 20 + (i//40)*30,
			fill = "gray",
			outline = "white"
		)

	total = time()-start
	try: framerate = int(1/total)
	except: framerate = 1000

	canvas.create_text(
		0, 0,
		font = ("Arial Black", 15, ""),
		fill = "yellow",
		anchor = "nw",
		text = str(framerate) + "fps\n" + str(total)
	)

	canvas.after(1, update)

update()

tk.mainloop()