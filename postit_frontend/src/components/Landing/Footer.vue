<script setup>
const aiServices = [
  {
    title: "AI Models",
    link: "#",
  },
  {
    title: "AI Analytics",
    link: "#",
  },
  {
    title: "AI for HR",
    link: "#",
  },
  {
    title: "AI Automation",
    link: "#",
  },
];

const aiTechnologies = [
  {
    title: "Machine Learning",
    link: "#",
  },
  {
    title: "Natural Language Processing",
    link: "#",
  },
  {
    title: "Deep Learning",
    link: "#",
  },
  {
    title: "Computer Vision",
    link: "#",
  },
];
</script>

<template>
  <div class="site-footer" style="background-color: #f4f7fc">
    <div class="footer-dots"></div>
    <div class="container">
      <div class="row justify-content-between">
        <div class="col-md-3">
          <div class="widget">
            <h3>AI Services</h3>
            <ul class="list-unstyled">
              <li v-for="(service, index) in aiServices" :key="index">
                <a :href="service.link">{{ service.title }}</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-md-3">
          <div class="widget">
            <h3>AI Technologies</h3>
            <ul class="list-unstyled">
              <li v-for="(tech, index) in aiTechnologies" :key="index">
                <a :href="tech.link">{{ tech.title }}</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-md-3">
          <div class="widget">
            <h3>Connect</h3>
            <ul class="list-unstyled">
              <li><a href="#">AI Forum</a></li>
              <li><a href="#">AI Community</a></li>
              <li><a href="#">AI Support</a></li>
            </ul>
          </div>
        </div>
        <div class="col-md-3">
          <div class="widget">
            <h3>Contact</h3>
            <address>1234 Street, City, Country</address>
            <ul class="list-unstyled">
              <li><a href="tel:+15551234567">+216 77777777</a></li>
              <li><a href="mailto:ai@example.com">ai@example.com</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div class="row justify-content-center mt-3">
        <div class="col-12 text-center">
          <p style="font-size: 12px">Copyright 2025, All rights reserved.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.site-footer {
  padding: 15px 0;
}

.widget h3 {
  font-size: 14px;
  margin-bottom: 10px;
}

.widget p, .widget address, .widget a {
  font-size: 12px;
}

@media (max-width: 768px) {
  .row {
    text-align: center;
  }

  .col-md-3 {
    margin-bottom: 10px;
  }
}
</style>
