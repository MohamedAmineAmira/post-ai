<script setup>
import mainPhoto from "@/assets/images/hero-logo.png";
import { themeColor } from "@/data/items";

const heroHeading = "Create Media Posts with AI";
const buttonSeeFeature = "Explore Features";

</script>

<template>
  <div class="untree_co-hero" id="home-section">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-12">
          <div class="dots"></div>
          <div class="row align-items-center">
            <div class="col-lg-7 ml-auto order-lg-2" data-aos="fade-right" data-aos-delay="400">
              <img :src="mainPhoto" alt="Image" class="img-fluid" />
            </div>
            <div class="col-lg-5">
              <h1 class="heading" data-aos="fade-up" data-aos-delay="0">
                {{ heroHeading }}
              </h1>
              <div class="excerpt" data-aos="fade-up" data-aos-delay="100">
                <p>
                  Easily generate engaging and creative media posts using AI. Save time,
                  enhance your content, and maximize your social media impact with smart AI-powered post generation.
                </p>
              </div>
              <p data-aos="fade-up" data-aos-delay="200">
                <a href="#features-section" class="btn btn-primary smoothscroll" style="margin-right: 5px" :style="[
                  { background: themeColor },
                  { borderColor: themeColor },
                ]">{{ buttonSeeFeature }}</a>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
