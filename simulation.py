from numpy.random import choice, exponential
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from os.path import exists
from os import makedirs

import time

def simulation(n0, m0, r1, r2, k1, k2, b1, b2, time_length, how_many_points=10, min_t=0.1, scaled = False):
    """
    Generator danych symulacji

    :param n0: początkowa liczebość pierwszego gatunku
    :param m0: początkowa liczebość drugiego gatunku
    :param v:  współczynnik rozrostu - odpowiada za częstość zmian stanu
    :param r1,r2,k1,k2,b1,b2: jak w modelu
    :param time_length: czas trwania symulacji
    :param how_many_points: jak często będziemy zapisywać punkty z symulacji, punkty są rozdzielone równo w czasie
        (gdyż czasem wiele zmian może dojśc w krótkim interwale)
    :param min_t: minimalna długośc interwału - środek zapobiegawczy przed wybuchnięciem procesu
    :return: zwracamy dane symulacji, czyli funkcję liczebności w czasie
                jeśli scaled = True to zwraca dane znormalizowane do limitów środowiska
    """
    jump_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    n, m, t = n0, m0, 0
    out = {"n": [n0], "m": [m0], "t": [t]}
    counter = 0

    while t < time_length:
        prob = [r1 * n, r2 * m, n * r1 * (n + b1 * m) / k1, m * r2 * (m + b2 * n) / k2]
        lam = sum(prob)
        if lam ==0.0:
            jump = (0, 0)
            interval = min_t
        else:
            prob = [e / lam for e in prob]
            jump = jump_list[int(choice(4, p=prob))]
            interval = max(exponential(scale=1/lam, size=None), min_t)
        t += interval
        counter += interval
        n, m = n+jump[0], m+jump[1]

        while counter > time_length/how_many_points:
            out["n"].append(n)
            out["m"].append(m)
            out["t"].append(t)
            counter -= time_length/how_many_points
    if scaled:
        out["n"] = [n / k1 for n in out["n"]]
        out["m"] = [m / k2 for m in out["m"]]
        out["t"] = [t * r1 for t in out["t"]]
    return out


def single_simulation():
    """
    Funkcja tworzy wykres pojedynczej symulacji
    """
    trajectory = simulation(n0=20, m0=10,
                            r1=10, r2=10, k1=100, k2=100,
                            b1=1, b2=1, time_length=10000, how_many_points=50)

    plt.plot(trajectory["n"], trajectory["m"], c="black", alpha=0.5)
    plt.scatter(trajectory["n"], trajectory["m"], c=trajectory["t"], marker='.', cmap='jet')
    plt.show()


def n_simulation(n, time_length, points):
    """
        Funkcja tworzy wykres n symulacji na tych samych parametrach
    """
    for i in range(n):
        trajectory = simulation(n0=20, m0=10, v=1,
                                r1=10, r2=10, k1=100, k2=100,
                                b1=1, b2=1, time_length=time_length, how_many_points=points)
        plt.plot(trajectory["n"], trajectory["m"], c="black", alpha=0.5)
        plt.scatter(trajectory["n"], trajectory["m"], c=trajectory["t"], marker='.', cmap='jet')
    plt.show()

def animated_simulation(sim_num = None, num_steps = 50, init_pos = None, time_len = 10000, max_initial=None, r1=10, r2=10, k1=100, k2=100, b1=1, b2=1, scaled = False,show = False):
    """
    Funkcja tworzy animację symulacji i zapisuje ją do gif-a.

    :param sim_num: liczba przeprowadzonych symulacji
    :param num_steps: rozdzielczość symulacji, tzn. liczba punktów które zostaną narysowane dla pojedynczej symulacji
    :param time_len: długośc trwania każdej symulacji
    :param max_initial: maksymalna wartość początkowych liczebności, które będzeimy losować,
        należy pamiętać że jeśli liczebność będzie znacznie większa od parametru środowiskowego k1 i k2
        to dojdzie do szybkiej korekty
    """
    if init_pos is None:
        init_pos = np.random.randint(1, max_initial, size=(2, sim_num))
        if sim_num is None:
            raise Exception("nie podana liczba symulacji")
    else:
        sim_num = len(init_pos[0])
    positions = np.ndarray(shape=(num_steps, 2, sim_num))
    init_pos = np.array(init_pos)

    trajectory_t = []
    for j in range(sim_num):
        start_time = time.time()
        trajectory = simulation(n0=init_pos[0, j], m0=init_pos[1, j],
                                r1=r1, r2=r2, k1=k1, k2=k2, b1=b1, b2=b2,
                                time_length=time_len, how_many_points=num_steps,
                                scaled=scaled)
        trajectory_t.append(time.time() - start_time)
        x = trajectory['n']
        y = trajectory['m']
        for i in range(num_steps):
            positions[i, 0, j] = x[i]
            positions[i, 1, j] = y[i]
    #DEBUG time
    print(f"Avg: {sum(trajectory_t)/len(trajectory_t)}")
    print(f"Max: {max(trajectory_t)}")
    print(f"Min: {min(trajectory_t)}")

    start_render_time = time.time()
    nframes, _, nparticles = positions.shape
    xylim = positions.max() * 1.2
    # Create figure
    fig, ax = plt.subplots(figsize=(5, 5))
    pts = [ax.plot([], [], "-o", alpha=0.5)[0]
           for j in range(nparticles)]

    # Plot initial particle positions
    def init():
        r0 = positions[0, :, :]
        for jj, p in enumerate(pts):
            p.set_data(r0[0, jj], r0[1, jj])
        # Set plot appearance
        ax.set_xlim([0, xylim])
        ax.set_ylim([0, xylim])
        return (pts)

    # Update particle positions
    def move(k):
        for jj, p in enumerate(pts):
            r = positions[:k + 1, :, jj]
            p.set_data(r[:, 0], r[:, 1])
            p.set_markevery((k, k + 1))
        return (pts)
    plt.xlabel("Gatunek 1")
    plt.ylabel("Gatunek 2")
    plt.title(f"Konkurencja gatunków\nr1={r1}, r2={r2},\n k1={k1}, k2={k2}, b12={b1}, b21={b2}")
    a12 = b1 * k2 / k1
    a21 = b2 * k1 / k2
    if scaled:
        plt.title(f"Konkurencja gatunków\na12={a12}, a21={a21}")
    plt.grid(True)
    ani = animation.FuncAnimation(fig, move, init_func=init,
                              interval=50, blit=True, save_count=15000)
    # izokliny

    if scaled:
        x_temp = np.array([0, 1, 2])
        plt.plot(x_temp, 1 - a21 * x_temp, '-.', linewidth=2, alpha=0.5)
        plt.plot(x_temp, (1 - x_temp)/a12, '-.', linewidth=2, alpha=0.5)
    else:
        x_temp = np.array(range(0, int(xylim), 3))
        plt.plot(x_temp, k2 - x_temp * b2, '-.', linewidth=2, alpha=0.5)
        plt.plot(x_temp, (k1 - x_temp) / b1, '-.', linewidth=2, alpha=0.5)
    file_index = 0
    if not exists(f'renders'):
        makedirs(f'renders')

    while(exists(f'renders/comp{str(file_index).zfill(5)}.mp4')):
        file_index+=1
    ani.save(f'renders/comp{str(file_index).zfill(5)}.mp4', bitrate=9, fps = 30, dpi = 400)
    print(f"Rendering: {time.time()-start_render_time}\n")












