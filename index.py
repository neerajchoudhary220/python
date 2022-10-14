from tkinter import*
from physio import physio_open
from primecoach import prime_coach
from changephpversion import changeversion

window = Tk()
window.title("All")
window.geometry("400x400")
window.resizable(FALSE, FALSE)
btn = Button(window, text="Open Physio", bg="green", fg="white",command=physio_open.physio.open)
btn.grid(column=0,row=1,padx=2)
btn2 = Button(window,text="Open Prime Coach", bg="green", fg="white",command=prime_coach.primecoach.open)
btn2.grid(column=1,row=1)
btn1= Button(window, text="Run Physio", bg="red", fg="white",command=physio_open.physio.run)
btn1.grid(column=2, row=1,padx=1)
btn3 = Button(window,text="Run Prime Coach", bg="red",fg="white",command=prime_coach.primecoach.run)
btn3.grid(column=3,row=1,padx=1)
btn4 = Button(window,text="Change Php v 8.1.6", bg="orange",fg="white",command=changeversion.phpversion.set_version_8_1_6)
btn4.grid(column=1,row=3,padx=2,pady=2)
btn5 = Button(window,text="Change Php v 7.4.0", bg="orange",fg="white",command=changeversion.phpversion.set_version_7_4_0)
btn5.grid(column=2,row=3,padx=2,pady=2)
window.mainloop()
