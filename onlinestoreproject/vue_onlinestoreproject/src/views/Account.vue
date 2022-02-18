<template>
  <div class="grid md:grid-cols-3">
    <div></div>
    <form
      class="items-center p-5 m-5 shadow-lg"
      @submit.prevent="submitForm"
      method="post"
    >
      <h3 class="text-xl font-medium text-gray-900 dark:text-white mb-2">
        {{ formData.heading }}
      </h3>
      <div v-for="(data, type) in formData.form" :key="type">
        <label for="type" class="form-label">{{ data.label }}</label>
        <input
          class="form-input"
          :type="data.type"
          :name="type"
          :id="type"
          :placeholder="data.placeholder"
        />
      </div>
      <div v-for="error in errors" :key="error">
        <p class="text-red-700 text-sm font-medium capitalize">
          {{ error }}
        </p>
      </div>
      <button type="submit" class="form-submit-button justify-start">
        {{ formData.buttonText }}
      </button>
      <div class="text-sm font-medium text-gray-500 dark:text-gray-300 mt-2">
        {{ formData.info.text }}

        <button
          type="button"
          class="text-red-700 hover:underline dark:text-red-500"
          @click="setFormData"
        >
          {{ formData.info.link }}
        </button>
      </div>
      <p class="text-red-700 text-sm font-medium capitalize pt-5 text-center">
        {{ error }}
      </p>
      <button
        v-if="this.$store.state.isAuthenticated"
        class="
          text-white
          bg-gray-500
          hover:bg-gray-700
          font-medium
          rounded
          text-sm
          px-5
          py-2.5
          text-center
          mt-2
        "
        @click="logout"
      >
        Logout
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Account",
  mounted() {
    this.setFormData();
  },
  data() {
    return {
      loginForm: false,
      formData: { form: {}, buttonText: "", info: {}, heading: "" },
      buttonText: "",
      error: "",
    };
  },
  methods: {
    logout() {
      // console.log("logging out");
      axios
        .post("/api/account/logout")
        .then((response) => {
          axios.defaults.headers.common["Authorization"] = "";
          localStorage.removeItem("token");
          this.$store.commit("REMOVE_TOKEN");
          this.$router.push("/");
        })
        .catch((error) => {
          if (error.response) console.log(JSON.stringify(error.response.data));
          else if (error.message) console.log(JSON.stringify(error.message));
          else console.log(JSON.stringify(error));
        });
    },
    login(email, password) {
      const formData = {
        username: email,
        password: password,
      };
      console.log(formData);
      axios
        .post("/api/account/login", formData)
        .then((response) => {
          const token = response.data["token"];
          this.$store.commit("SET_TOKEN", token);
          axios.defaults.headers.common["Authorization"] = "Token " + token;
          localStorage.setItem("token", token);
          this.$router.push("/");
        })
        .catch((error) => {
          for (const property in error.response.data) {
            this.error = error.response.data[property][0];
            break;
          }
        });
    },
    submitForm(e) {
      this.error = "";
      if (!this.$store.state.isAuthenticated) {
        if (this.loginForm) {
          const email = document.querySelector("#email").value;
          const password = document.querySelector("#password").value;
          this.login(email, password);
        } else {
          const formData = {
            username: document.querySelector("#username").value,
            email: document.querySelector("#email").value,
            password: document.querySelector("#password").value,
            password2: document.querySelector("#password2").value,
          };
          axios
            .post("/api/account/register", formData)
            .then((response) => {
              this.login(formData["email"], formData["password"]);
              // this.$router.push("/");
            })
            .catch((error) => {
              for (const property in error.response.data) {
                this.error = error.response.data[property][0];
              }
            });
        }
      }
    },
    setFormData() {
      this.error = "";
      if (!this.$store.state.isAuthenticated) {
        this.loginForm = !this.loginForm;
        if (this.loginForm) {
          this.formData = {
            heading: "Sign in to your account",
            form: {
              email: {
                label: "Email",
                type: "email",
                placeholder: "user@example.com",
              },
              password: {
                label: "Password",
                type: "password",
                placeholder: "••••••••",
              },
            },
            buttonText: "Sign in to your account",
            info: {
              text: "Dont' have an account?",
              link: "Create account",
            },
          };
        } else {
          this.formData = {
            heading: "Register a new account",
            form: {
              username: {
                label: "Username",
                type: "text",
                placeholder: "Username",
              },
              email: {
                label: "Email",
                type: "email",
                placeholder: "user@example.com",
              },
              password: {
                label: "Password",
                type: "password",
                placeholder: "••••••••",
              },
              password2: {
                label: "Confirm Password",
                type: "password",
                placeholder: "••••••••",
              },
            },
            buttonText: "Create new account",
            info: {
              text: "Already have an account?",
              link: "Sign in",
            },
          };
        }
      } else {
        axios
          .get("/api/account/get-user-profile")
          .then((response) => {
            this.formData = {
              heading: "Your profile",
              form: {
                firstName: {
                  label: "First Name",
                  type: "text",
                  placeholder: response.data["first_name"],
                },
                lastName: {
                  label: "Last Name",
                  type: "text",
                  placeholder: response.data["last_name"],
                },
                phone: {
                  label: "Phone Number",
                  type: "number",
                  placeholder: response.data["last_name"],
                },
              },
              buttonText: "Update Information",
              info: {
                text: "",
                link: "Change Password",
              },
            };
          })
          .catch((error) => {
            this.error = "Error fetching user data";
          });
      }
    },
  },
};
</script>