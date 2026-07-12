import sys

with open('src/components/PublicationsList.tsx', 'r') as f:
    content = f.read()

# 1. Update empirical projects card
empirical_motion_div_old = """                <motion.div 
                  key={p.id} 
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true, margin: "-50px" }}
                  transition={{ duration: 0.4, delay: idx * 0.1 }}
                  style={{ perspective: "1000px" }}
                >
                  <div
                    style={{ transformStyle: "preserve-3d" }}
                    className={`p-8 border flex flex-col justify-between transition-all duration-500 hover:-translate-y-2 hover:rotate-x-2 hover:rotate-y-2 hover:shadow-2xl h-full ${"""

empirical_motion_div_new = """                <motion.div 
                  key={p.id} 
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  whileHover={{ y: -8, rotateX: 2, rotateY: -2, scale: 1.01 }}
                  viewport={{ once: true, margin: "-50px" }}
                  transition={{ duration: 0.4, delay: idx * 0.1 }}
                  style={{ perspective: "1000px" }}
                >
                  <div
                    style={{ transformStyle: "preserve-3d" }}
                    className={`p-8 border flex flex-col justify-between transition-all duration-500 hover:shadow-2xl h-full ${"""

content = content.replace(empirical_motion_div_old, empirical_motion_div_new)

# 2. Update PublicationCard
pub_motion_div_old = """    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: "-50px" }}
      transition={{ duration: 0.4, delay: index * 0.1 }}
      style={{ perspective: "1000px" }}
    >
      <div
        onClick={toggleExpand}
        style={{ 
          transformStyle: "preserve-3d",
          transform: isExpanded ? "rotateX(2deg) rotateY(-2deg) scale(1.02)" : "rotateX(0deg) rotateY(0deg) scale(1)"
        }}
        className={`p-6 border transition-all duration-500 cursor-pointer hover:-translate-y-2 hover:rotate-x-2 hover:-rotate-y-2 hover:shadow-2xl ${"""

pub_motion_div_new = """    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      whileHover={{ y: -8, rotateX: 2, rotateY: -2, scale: 1.01 }}
      viewport={{ once: true, margin: "-50px" }}
      transition={{ duration: 0.4, delay: index * 0.1 }}
      style={{ perspective: "1000px" }}
    >
      <div
        onClick={toggleExpand}
        style={{ 
          transformStyle: "preserve-3d",
          transform: isExpanded ? "rotateX(2deg) rotateY(-2deg) scale(1.02)" : "rotateX(0deg) rotateY(0deg) scale(1)"
        }}
        className={`p-6 border transition-all duration-500 cursor-pointer hover:shadow-2xl ${"""

content = content.replace(pub_motion_div_old, pub_motion_div_new)

# 3. Update Kaggle banner to tilt on hover
kaggle_banner_old = """        {/* Kaggle Creative Banner */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-50px" }}
          transition={{ duration: 0.6 }}
          className={`mt-16 md:col-span-2 relative overflow-hidden p-8 md:p-12 border ${"""

kaggle_banner_new = """        {/* Kaggle Creative Banner */}
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

content = content.replace(kaggle_banner_old, kaggle_banner_new)

# Since we wrapped the Kaggle banner content in another div, we need to add a closing div for it
# The kaggle banner ends with:
#             <NeuralNetworkButton href="https://www.kaggle.com/georgeokello/" isDark={isDark} />
#           </div>
#         </motion.div>
#       </div>

kaggle_banner_end_old = """            <NeuralNetworkButton href="https://www.kaggle.com/georgeokello/" isDark={isDark} />
          </div>
        </motion.div>
      </div>"""

kaggle_banner_end_new = """            <NeuralNetworkButton href="https://www.kaggle.com/georgeokello/" isDark={isDark} />
          </div>
          </div>
        </motion.div>
      </div>"""

content = content.replace(kaggle_banner_end_old, kaggle_banner_end_new)

with open('src/components/PublicationsList.tsx', 'w') as f:
    f.write(content)

