<script setup>
import { ref, computed } from "vue";
import { themeColor } from "../data/items";
import axiosInstance from "../services/axiosInstance";
import router from '../router';


const register = ref({
  full_name: "",
  email: "",
  password: "",
});

const errors = ref({
  full_name: null,
  email: null,
  password: null,
});

const isRegisterDisabled = computed(() => {
  return !register.value.full_name || !register.value.email || !register.value.password;
});

async function Register() {
  try {
    const response = await axiosInstance.post("api/auth/register/", register.value);
    console.log("Registration successful:", response.token); 
    localStorage.setItem('token', response.token);
    router.push({ path: '/home' })
  } catch (error) {
    if (error.response) {
      errors.value = error.response;  
    } else {
      console.error("Unexpected error:", error);
    }
  }
}


</script>

<template>
  <div style="background-color: #f4f7fc; min-height: 100vh;">
    <div class="untree_co-section d-flex justify-content-center align-items-center vh-100">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-6">
            <div class="text-center mb-4">
              <h2 class="heading">Register</h2>
              <p>Create your account to get started.</p>
            </div>
            <form class="registration-form p-4 shadow rounded bg-white" @submit.prevent="Register" data-aos="fade-up"
              data-aos-delay="100">
              <div class="form-group">
                <label for="fullName">Full Name</label>
                <input type="text" v-model="register.full_name" class="form-control" id="fullName" required />
                <p v-if="errors.full_name" class="text-danger">{{ errors.full_name[0] }}</p>
              </div>

              <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" v-model="register.email" class="form-control" id="email" required />
                <p v-if="errors.email" class="text-danger">{{ errors.email[0] }}</p>
              </div>

              <div class="form-group">
                <label for="password">Password</label>
                <input type="password" v-model="register.password" class="form-control" id="password" required />
                <p v-if="errors.password" class="text-danger">{{ errors.password[0] }}</p>
              </div>

              <button :disabled="isRegisterDisabled" type="submit" class="btn btn-primary w-100"
                :style="[{ backgroundColor: themeColor }, { borderColor: themeColor }]">
                Register
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
