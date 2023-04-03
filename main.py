import simulation as sim


def mul_all(l, k):
    return [el*k for el in l]


if __name__ == '__main__':
    big_scale_cases = [[1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 100, 200, 300, 400, 500, 600, 700, 800, 900],
                        [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]]
    small_scale_cases = [[1,1,1,1,2,2,3,4,3],
                         [1,2,3,4,3,1,1,1,2]]
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=10, scaled=False, time_len=10,
                            r1=9, r2=11, k1=20, k2=20, b1=2, b2=3)
    


"""
    k = 1
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=9, r2=11,
                            k1=1000, k2=1000,
                            b1=3, b2=0.8)

    k = 10
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=50000, scaled=False, time_len=100000,
                            r1=20, r2=20, k1=10000, k2=10000, b1=2, b2=3)
    sim.animated_simulation(init_pos=cases, num_steps=50000, scaled=False, time_len=100000,
                            r1=20, r2=20, k1=10000, k2=10000, b1=1.5, b2=0.3)
    sim.animated_simulation(init_pos=cases, num_steps=50000, scaled=False, time_len=100000,
                            r1=20, r2=20, k1=10000, k2=10000, b1=0.7, b2=2)
    sim.animated_simulation(init_pos=cases, num_steps=50000, scaled=False, time_len=100000,
                            r1=20, r2=20, k1=10000, k2=10000, b1=0.6, b2=0.3)

    k = 2
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=5, r2=5,
                            k1=1000, k2=2000,
                            b1=1.5, b2=0.3)
    k = 1.5
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=10, r2=4,
                            k1=1300, k2=800,
                            b1=1.8, b2=0.5)
    k = 6.1
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=15, r2=12,
                            k1=5000, k2=6000,
                            b1=5, b2=1)

    k = 20
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=4, r2=4,
                            k1=10000, k2=20000,
                            b1=1.7, b2=1.8)
    k = 12
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=10, r2=20,
                            k1=11110, k2=12340,
                            b1=1, b2=1)
    k = 1
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=9, r2=11,
                            k2=1000, k1=1000,
                            b2=3.2, b1=2)
    k = 2
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=5, r2=5,
                            k2=1000, k1=2000,
                            b2=1.4, b1=0.35)
    k = 1.5
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=10, r2=4,
                            k2=1300, k1=800,
                            b2=1.7, b1=0.5)
    k = 6.1
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=15, r2=12,
                            k2=5000, k1=6000,
                            b2=4, b1=1.1)
    k = 20
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=4, r2=4,
                            k2=10000, k1=20000,
                            b2=1.6, b1=1.8)
    k = 12
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=10, r2=20,
                            k2=1100, k1=1434,
                            b2=1, b1=1)

    k = 1
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=9, r2=11,
                            k1=1000, k2=1000,
                            b1=3, b2=2)
    k = 2
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=5, r2=5,
                            k1=1000, k2=2000,
                            b1=1.5, b2=2.1)
    k = 1.5
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=10, r2=4,
                            k1=1300, k2=800,
                            b1=1.8, b2=1)
    k = 6.1
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=15, r2=12,
                            k1=5000, k2=6000,
                            b1=2, b2=2)

    k = 20
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=4, r2=4,
                            k1=10000, k2=20000,
                            b1=1.7, b2=2.5)
    k = 12
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=10, r2=20,
                            k1=11110, k2=12340,
                            b1=1, b2=1.5)

    k = 1
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=9, r2=11,
                            k1=1000, k2=1000,
                            b1=0.8, b2=0.5)
    k = 2
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=5, r2=5,
                            k1=1000, k2=2000,
                            b1=0.4, b2=1.6)
    k = 1.5
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=10, r2=4,
                            k1=1300, k2=800,
                            b1=1.1, b2=0.3)
    k = 6.1
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=15, r2=12,
                            k1=5000, k2=6000,
                            b1=0.8, b2=1)
    k = 20
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=4, r2=4,
                            k1=10000, k2=20000,
                            b1=0.2, b2=1.1)
    k = 12
    cases = [mul_all(big_scale_cases[0], k) + small_scale_cases[0],
             mul_all(big_scale_cases[1], k) + small_scale_cases[1]]
    sim.animated_simulation(init_pos=cases, num_steps=1000,
                            r1=10, r2=20,
                            k1=11110, k2=12340,
                            b1=0.5, b2=0.5)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=1000, scaled=False, time_len=1000,
                            r1=9, r2=11, k1=20, k2=20, b1=1.5, b2=0.3)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=1000, scaled=False, time_len=1000,
                            r1=9, r2=11, k1=20, k2=20, b1=0.7, b2=2)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=1000, scaled=False, time_len=1000,
                            r1=9, r2=11, k1=20, k2=20, b1=0.6, b2=0.3)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=1000, scaled=False, time_len=1000,
                            r1=9, r2=11, k1=10, k2=10, b1=0.1, b2=0.2)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=1000, scaled=False, time_len=1000,
                            r1=9, r2=11, k1=7, k2=5, b1=0.5, b2=0.2)

    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=20, k2=20, b1=2, b2=3)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=20, k2=20, b1=1.5, b2=0.3)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=20, k2=20, b1=0.7, b2=2)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=20, k2=20, b1=0.6, b2=0.3)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=10, k2=10, b1=0.1, b2=0.2)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=7, k2=5, b1=0.5, b2=0.2)

    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=7, k2=7, b1=2, b2=3)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=7, k2=7, b1=1.5, b2=0.3)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=7, k2=7, b1=0.7, b2=2)
    sim.animated_simulation(init_pos=small_scale_cases, num_steps=100000, scaled=False, time_len=10000,
                            r1=9, r2=11, k1=7, k2=7, b1=0.6, b2=0.3)
"""