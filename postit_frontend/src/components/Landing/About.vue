<script setup>
import { themeColor } from "@/data/items";
import mainPhoto from "@/assets/images/about-logo.png";

const heading = "About";
const subHeading = "About Post AI";
const totalMembers = "50";
const totalTeam = "20";
</script>

<template>
  <div class="untree_co-section" id="about-section">
    <div class="container">
      <div class="row justify-content-between">
        <div class="col-lg-8" data-aos="fade-up" data-aos-delay="100" style="display: block; margin: 0 auto;">
          <img :src="mainPhoto" alt="PostIt Logo" class="img-fluid" />
        </div>
        <div class="col-lg-4">
          <div class="mb-4" data-aos="fade-up" data-aos-delay="0">
            <span class="caption" :style="[{ color: themeColor }]">{{ heading }}</span>
            <h2 class="heading">{{ subHeading }}</h2>
          </div>
          <div class="mb-4" data-aos="fade-up" data-aos-delay="100">
            <p>
              PostIt is an AI-powered platform that generates social media posts tailored to your audience.
              Built with cutting-edge Generative AI models, PostIt makes it easy for users to create effective
              posts for social media, helping businesses and individuals boost engagement and brand presence.
            </p>
            <p>
              Our platform leverages powerful AI technologies to craft the perfect posts, making it simple
              for anyone to generate high-quality content, even without a background in content creation.
            </p>
          </div>
          <ul
            class="list-unstyled ul-check primary mb-4"
            data-aos="fade-up"
            data-aos-delay="200"
          >
            <li><i class=" check text-primary me-2"></i> AI-powered social media content generation</li>
            <li><i class=" check text-primary me-2"></i> User-friendly interface for all levels</li>
            <li><i class=" check text-primary me-2"></i> Focus on scalability and growth</li>
          </ul>
          <div class="row count-numbers">
            <div class="col-lg-6" data-aos="fade-up" data-aos-delay="0">
              <span class="counter d-block">
                <span :data-number="totalMembers">{{ totalMembers }}</span><span>M</span>
              </span>
              <span class="caption-2">
                <i class="bi bi-person-fill"></i> Users
              </span>
            </div>
            <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
              <span class="counter d-block">
                <span :data-number="totalTeam">{{ totalTeam }}</span>
              </span>
              <span class="caption-2">
                <i class="bi bi-person-check-fill"></i> Team
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
