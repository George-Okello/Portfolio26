import sys

with open('src/components/PublicationsList.tsx', 'r') as f:
    content = f.read()

kaggle_banner_old = """        {/* Kaggle Creative Banner */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          whileHover={{ y: -8, rotateX: 2, rotateY: -2, scale: 1.01 }}
          viewport={{ once: true, margin: "-50px" }}
          transition={{ duration: 0.6 }}
          style={{ perspective: "1000px" }}
        >
          <div
            style={{ transformStyle: "preserve-3d" }}
            className={`mt-16 md:col-span-2 relative overflow-hidden p-8 md:p-12 border transition-shadow duration-500 hover:shadow-2xl ${"""

kaggle_banner_new = """        {/* Kaggle Creative Banner */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-50px" }}
          transition={{ duration: 0.6 }}
          className={`mt-16 md:col-span-2 relative overflow-hidden p-8 md:p-12 border ${"""

content = content.replace(kaggle_banner_old, kaggle_banner_new)

kaggle_banner_end_old = """            <NeuralNetworkButton href="https://www.kaggle.com/georgeokello/" isDark={isDark} />
          </div>
          </div>
        </motion.div>
      </div>"""

kaggle_banner_end_new = """            <NeuralNetworkButton href="https://www.kaggle.com/georgeokello/" isDark={isDark} />
          </div>
        </motion.div>
      </div>"""

content = content.replace(kaggle_banner_end_old, kaggle_banner_end_new)

with open('src/components/PublicationsList.tsx', 'w') as f:
    f.write(content)

