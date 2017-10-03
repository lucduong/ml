import numpy as np
import tensorflow as tf

# ------ Say hello
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

# ------ Assign the constants
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0)  # also tf.float32 implicitly
print(node1, node2)

sess = tf.Session()
print(sess.run([node1, node2]))

# ------ Test the additional function
node3 = tf.add(node1, node2)
print("node3: ", node3)
print("sess.run(node3): ", sess.run(node3))

# ------ Define the variable without constant
n1 = tf.placeholder(tf.float32)
n2 = tf.placeholder(tf.float32)
adder_node = n1 + n2
print("adder_node: ", adder_node)

print("add: ", sess.run(adder_node, {n1: 5, n2: 7}))
print("add array: ", sess.run(adder_node, {n1: [1, 2], n2: [3, 4]}))

# ------ Multiple to 3
add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {n1: 3, n2:4.5}))

# ------ Initial Values
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W * x + b

init = tf.global_variables_initializer()
sess.run(init)

print(sess.run(linear_model, {x:[1,2,3,4]}))

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

file_writer = tf.summary.FileWriter('./logs/sample_adder_node', sess.graph)

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init) # reset values to incorrect defaults.
for i in range(1000):
    sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})
    print(sess.run([W, b]))


