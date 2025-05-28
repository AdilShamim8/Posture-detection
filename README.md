# Pose Detection with Face Overlays


Imagine a world where your computer sees you—not just as pixels, but as a living, breathing silhouette. Where art and technology dance seamlessly on your screen. Welcome to **Pose Detection with Face Overlays**, a simple yet magical Python 3.10 project that transforms your webcam feed into a playful canvas of expression.

---

## Experience the Magic

Witness real-time pose detection come alive. Each movement you make is embraced by fun, stylized masks:

![Pose with Overlay 1](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGNfQavEiYMs5I_9uJf03gy79HVgHd-dJUV-C7mgOMs6GF5Ll0s55CTORGS-PfiZ72Sc6WJQhbktAPc5Q8CuqTfRx1x4Fju779bSb_gE1F_2hjvnj61OcWDrvoRfInJsB18-SvxVtvTVY/s320/p1.gif)

![Pose with Overlay 2](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjvEKf4_UlEbL2uijUfYlz0tOsHjs2wvGs9RhW8k_zSORA0hNmp9ed6_cW_Vp8KfmG7SAfBphKzUX-jyBesqGumRBeIH1ekrJdcj12hZkjiBeYVv30IaLlmQztR3UxBJLCPPpE1cUWOC-Y/s320/p2.gif)


##  Why You’ll Love It

* **Real-Time Magic**: Powered by Mediapipe’s Pose model and OpenCV for lightning-fast landmark detection.
* **Playful Overlays**: Overlay any transparent mask or artwork—turn a simple webcam into a stage.
* **Effortless Setup**: Runs on Python 3.10. No rocket science required.
* **Endless Creativity**: Swap, add, or tweak overlays in seconds.

---

##  Get Started in 3 Steps

1. **Clone & Dive In**

   ```bash
   git clone https://github.com/AdilShamim8/Posture-detection.git
   cd Posture-detection
   ```
2. **Spark Your Environment**

   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   pip install -r requirements.txt
   ```
3. **Run the Show**

   ```bash
   python main.py
   ```

   Press `q` to exit the spotlight.

---

##  Peek Under the Hood

```
Posture-detection/
├── main.py           # Orchestrates pose detection & overlays
├── overlays/         # Directory with your overlay assets
└── requirements.txt  # Python dependencies
```

---

##  Customize Your Masterpiece

1. Drop your own PNG/GIF in `overlays/`.
2. In `main.py`, update:

   ```python
   OVERLAYS = ["face1.png", "face2.png", "my_artwork.png"]
   ```
3. Tweak sizes & positions to perfection.

---

##  Join the Journey

Contributions, feedback, wild ideas—bring them on!

1. Fork this repo
2. Create your vision (`git checkout -b my-feature`)
3. Commit brilliance (`git commit -m "Add epic overlay"`)
4. Share with the world (`git push origin my-feature`) & open a PR

---

## 📜 License & Contact

MIT License
Adil Shamim | [GitHub](https://github.com/AdilShamim8) | [adilshamim696@gmail.com](mailto:adilshamim696@gmail.com)
