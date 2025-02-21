<script setup>

const heading = "Why Choose Post AI?";
const subHeading = "Leverage AI to craft engaging and impactful social media posts effortlessly.";

const advantages = [
  {
    name: "Boost Your Online Presence",
    des: "Generate high-quality AI-powered content that resonates with your audience and increases engagement.",
    icon: "bi-graph-up-arrow",
  },
  {
    name: "Save Time & Effort",
    des: "Automate your content creation process and focus on strategy while AI handles the writing.",
    icon: "bi-clock-history", 
  },
  {
    name: "Enhance Creativity",
    des: "Get AI-generated suggestions, captions, and hashtags to make your posts more compelling.",
    icon: "bi-stars", 
  },
  {
    name: "Multi-Platform Optimization",
    des: "Customize and optimize content for various platforms like LinkedIn, Twitter, and Instagram in one click.",
    icon: "bi-share", 
  },
];
</script>

<template>
  <div class="untree_co-section" id="features-section">
    <div class="container">
      <div class="row mb-4">
        <div class="col-12 text-center" data-aos="fade-up" data-aos-delay="0">
          <h2 class="heading">{{ heading }}</h2>
          <p>{{ subHeading }}</p>
        </div>
      </div>
      <div class="row">
        <div 
          class="col-lg-6 mb-4" 
          v-for="(advantage, index) in advantages" 
          :key="index" 
          data-aos="fade-up" 
          :data-aos-delay="100 * (index + 1)"
        >
          <div class="service horizontal d-flex align-items-center">
            <div class="service-icon mb-4 me-3">
              <i :class="`bi ${advantage.icon} text-primary fs-2`"></i>
            </div>
            <div class="service-contents">
              <h3>{{ advantage.name }}</h3>
              <p>{{ advantage.des }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
