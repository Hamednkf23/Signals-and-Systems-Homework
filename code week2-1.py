# ==============================
# سیگنال‌ها - مثال‌های 3، 4، 5 و 6
# درس سیگنال‌ها و سیستم‌ها
# ==============================


# تنظیم ظاهر نمودارها
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.grid'] = True
plt.rcParams['figure.figsize'] = (10, 6)

# ==============================
# مثال 3 - سیگنال پیوسته x(t) = Π(t)
# ==============================

def rect(t):
    """تابع مستطیلی Π(t)"""
    return np.where(np.abs(t) <= 0.5, 1, 0)

t = np.linspace(-3, 3, 1000)
x_t = rect(t)
y1_t = rect(t + 0.5)
y2_t = rect(t - 2)

plt.figure()
plt.subplot(3,1,1)
plt.plot(t, x_t)
plt.title('مثال 3: x(t) = Π(t)')
plt.ylabel('x(t)')

plt.subplot(3,1,2)
plt.plot(t, y1_t)
plt.ylabel('y1(t) = x(t + 0.5)')

plt.subplot(3,1,3)
plt.plot(t, y2_t)
plt.ylabel('y2(t) = x(t - 2)')
plt.xlabel('t')
plt.tight_layout()
plt.show()


# ==============================
# مثال 4 - سیگنال گسسته x[n]
# ==============================

n = np.arange(-2, 2)
x_n = np.array([-2, 1, 1, -1])

y1_n = np.roll(x_n, 3) # x[n + 3]
y2_n = np.roll(x_n, -1) # x[n - 1]

plt.figure()
plt.subplot(3,1,1)
plt.stem(n, x_n, use_line_collection=True)
plt.title('مثال 4: x[n]')
plt.ylabel('x[n]')

plt.subplot(3,1,2)
plt.stem(n, y1_n, use_line_collection=True)
plt.ylabel('y1[n] = x[n + 3]')

plt.subplot(3,1,3)
plt.stem(n, y2_n, use_line_collection=True)
plt.ylabel('y2[n] = x[n - 1]')
plt.xlabel('n')
plt.tight_layout()
plt.show()


# ==============================
# مثال 5 - وارون‌سازی زمانی در سیگنال پیوسته
# ==============================

T = 2
t = np.linspace(-3, 3, 500)
x_t = np.where((t >= -T/2) & (t <= T/2), 1, 0)
y_t = np.where((-t >= -T/2) & (-t <= T/2), 1, 0)

plt.figure()
plt.subplot(2,1,1)
plt.plot(t, x_t)
plt.title('مثال 5: وارون‌سازی زمانی')
plt.ylabel('x(t)')

plt.subplot(2,1,2)
plt.plot(t, y_t)
plt.ylabel('y(t) = x(-t)')
plt.xlabel('t')
plt.tight_layout()
plt.show()


# ==============================
# مثال 6 - وارون‌سازی زمانی در سیگنال گسسته
# ==============================

n = np.arange(-2, 3)
x_n = np.array([-1, 2, 3, 1, 0])
y_n = x_n[::-1] # وارون‌سازی

plt.figure()
plt.subplot(2,1,1)
plt.stem(n, x_n, use_line_collection=True)
plt.title('مثال 6: وارون‌سازی زمانی گسسته')
plt.ylabel('x[n]')

plt.subplot(2,1,2)
plt.stem(n, y_n, use_line_collection=True)
plt.ylabel('y[n] = x[-n]')
plt.xlabel('n')
plt.tight_layout()
plt.show()
