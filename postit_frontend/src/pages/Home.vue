<script setup>
import { ref, computed } from 'vue'
import { themeColor } from "../data/items"
import axiosInstance from "../services/axiosInstance";
import router from '../router';


const heading = "Create Media Posts with AI"
const subHeading = "Easily generate your media posts using AI technology."

const generatedText = ref('')
const formData = ref({
    context: "",
});

// Fix: Corrected computed property
const isFormDisabled = computed(() => !formData.value.context.trim());

const generatePost = async () => {
    try {
        const response = await axiosInstance.post("api/post/generate_post/", formData.value);
        generatedText.value = response.generated_post;
    } catch (error) {
        console.error("Unexpected error:", error);
    }
}

const signOut = () => {
    localStorage.removeItem("token");
    router.push({ path: '/' }); 
};

const copyText = async () => {
    try {
        await navigator.clipboard.writeText(generatedText.value);
        console.log("Text copied successfully!");
    } catch (err) {
        console.error("Failed to copy text:", err);
    }
}

const downloadText = () => {
    const blob = new Blob([generatedText.value], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'generated_text.txt';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
</script>

<template>
    <nav class="site-nav dark js-site-navbar mb-5 site-navbar-target">
        <div class="container">
            <div class="site-navigation">
                <a href="" class="logo m-0 float-left">Post AI<span class="text-primary">.</span></a>
                <ul class="js-clone-nav d-none mt-1 d-lg-inline-block site-menu float-right">
                    <li class="cta-button-outline" style="margin-right: 5px;"><a href="#" @click="signOut">Sign out</a></li>
                </ul>
                <a href="#" class="burger ml-auto float-right site-menu-toggle js-menu-toggle d-inline-block dark d-lg-none"
                    data-toggle="collapse" data-target="#main-navbar">
                    <span></span>
                </a>
            </div>
        </div>
    </nav>

    <div class="untree_co-section" id="contact-section" style="background-color: #f4f7fc; min-height: 100vh;">
        <div class="container">
            <div class="row mb-4 text-center" data-aos="fade-up" data-aos-delay="0">
                <div class="col-12">
                    <h2 class="heading">{{ heading }}</h2>
                    <p>{{ subHeading }}</p>
                </div>
            </div>

            <div class="row justify-content-center">
                <!-- Left side: Message Input Form -->
                <div class="col-lg-5">
                    <form class="contact-form" @submit.prevent="generatePost" data-aos="fade-up" data-aos-delay="100">
                        <div class="form-group d-flex mb-2">
                            <textarea v-model="formData.context" name="context" class="form-control shadow-lg" id="context"
                                rows="8"
                                style="border-radius: 12px; resize: none; border: 1px solid #ccc; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%;"
                                placeholder="Enter your context here"></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary w-100 mt-2" :disabled="isFormDisabled"
                            :style="{ backgroundColor: themeColor, borderColor: themeColor }">
                            Send Context
                        </button>
                    </form>
                </div>

                <!-- Right side: Generated Text -->
                <div class="col-lg-5 mt-4 mt-lg-0">
                    <div data-aos="fade-up" data-aos-delay="200">
                        <textarea v-model="generatedText" name="generatedText" class="form-control shadow-lg"
                            id="generatedText" rows="8"
                            style="border-radius: 12px; resize: none; border: 1px solid #ccc; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); width: 100%;"
                            readonly placeholder="Generated text will appear here"></textarea>

                        <!-- Buttons aligned in a single row with space between -->
                        <div class="mt-3 d-flex justify-content-between">
                            <!-- Copy Button -->
                            <button class="btn btn-secondary btn-sm" @click="copyText"
                                :style="{ backgroundColor: themeColor, borderColor: themeColor }">
                                <i class="bi bi-clipboard" style="font-size: 1rem; color: white;"></i>
                            </button>

                            <!-- Download Button -->
                            <button class="btn btn-secondary btn-sm" @click="downloadText"
                                :style="{ backgroundColor: themeColor, borderColor: themeColor }">
                                <i class="bi bi-download" style="font-size: 1rem; color: white;"></i>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.btn-sm {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
}

.form-control {
    border-radius: 12px;
    border: 1px solid #ccc;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.heading {
    font-weight: bold;
    font-size: 2rem;
}

.btn i {
    font-size: 1rem;
}

.container {
    max-width: 100%;
}

.mt-3 {
    margin-top: 1rem;
}
</style>
