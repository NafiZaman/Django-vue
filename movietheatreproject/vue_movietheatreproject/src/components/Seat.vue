<template>
  <div>
    <div class="row">
      <div class="mt-3 col" style="margin-left: 25rem; margin-right: 25rem">
        <div class="d-flex flex-column">
          <div>
            <p class="mb-0 h4"><strong>2. Select Seat(s)</strong></p>
          </div>
        </div>
      </div>
    </div>
    <div>
      <hr />
      <div
        class="card border border-danger"
        style="margin-left: 25rem; margin-right: 25rem"
      >
        <div class="card-body">
          <p class="mb-5 display-5 text-center">Movie Screen</p>
          <!-- Seat selection starts here -->
          <div
            class="btn-group d-flex flex-row"
            role="group"
            aria-label="Basic checkbox toggle button group"
          >
            <div class="d-flex flex-column" v-for="i in theatreCol" :key="i">
              <div class="d-flex flex-row" v-for="j in section1" :key="j">
                <input
                  type="checkbox"
                  class="btn-check"
                  autocomplete="off"
                  :id="i + j"
                />
                <label class="me-2 mt-2 btn btn-outline-success" :for="i + j">{{
                  i + j
                }}</label>
              </div>
            </div>
            <div class="mx-auto"></div>
            <div class="d-flex flex-column" v-for="k in theatreCol" :key="k">
              <div class="d-flex flex-row" v-for="l in section2" :key="l">
                <input
                  type="checkbox"
                  class="btn-check"
                  autocomplete="off"
                  :id="k + l"
                  @click="selectSeat"
                />
                <label class="me-2 mt-2 btn btn-outline-primary" :for="k + l">{{
                  k + l
                }}</label>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col" style="margin-left: 25rem; margin-right: 25rem">
        <div class="mt-5 d-flex justify-content-center">
          <button class="px-5 btn-lg btn-danger" @click="proceedToNextStep">
            NEXT
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Seat",
  mounted() {
    this.getMaxSeats();
  },
  data() {
    return {
      section1: ["a", "b", "c", "d", "e", "f"],
      section2: ["g", "h", "i", "j", "k", "l"],
      theatreCol: 6,
      maxSeats: 0,
      selectedSeats: [],
      seatString: "",
    };
  },
  mounted() {
    this.getMaxSeats();
    this.proceedToNextStep();
  },
  methods: {
    getMaxSeats() {
      const ticket = JSON.parse(localStorage.getItem("ticket"));
      this.maxSeats +=
        ticket.Adult.count + ticket.Child.count + ticket.Senior.count;
    },
    selectSeat(event) {
      const seatID = event.currentTarget.id;
      if (this.selectedSeats.includes(seatID)) {
        var index = this.selectedSeats.indexOf(seatID);
        this.selectedSeats.splice(index, 1);
      } else if (this.selectedSeats.length < this.maxSeats)
        this.selectedSeats.push(seatID);
      else {
        event.currentTarget.checked = false;
      }
    },
    proceedToNextStep(event) {
      if (localStorage.getItem("seat")) {
        this.selectedSeats = localStorage.getItem("seat");
        this.$store.commi("setSeat", this.selectedSeats);
        this.seatString = this.selectedSeats.join();
      } else if (this.selectedSeats.lenght === this.maxSeats) {
        this.$store.commit("setSeat", this.selectedSeats);
        this.seatString = this.selectedSeats.join();
      }
    },
  },
};
</script>