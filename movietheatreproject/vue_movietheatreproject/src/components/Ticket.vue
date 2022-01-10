<template>
  <div>
    <section>
      <div class="mb-2 row border-bottom border-danger border-3 text-md-center">
        <div class="mt-3 col">
          <p class="mb-0 h6"><strong>Number of Ticket(s)</strong></p>
          <p class="mb-2">
            <small>You can reserve upto 5 seats per booking</small>
          </p>
        </div>
      </div>
    </section>

    <div v-if="!bookingData.ticket">
      <div
        class="row justify-content-center"
        v-for="(data, ticketType) in ticket"
        :key="ticketType"
      >
        <div class="col col-md-6">
          <p class="mb-0 h6">
            {{ ticketType }}
          </p>
          <p class="text-muted lh-1">
            <small>&#2547;{{ data.price }}</small>
          </p>
        </div>
        <div class="col-auto">
          <div class="d-flex">
            <button
              class="p-0 btn btn-lg text-danger"
              @click="increaseTicketTypeCount(data, 'remove')"
            >
              <i class="bi bi-dash-circle"></i>
            </button>
            <p class="m-2 h6">
              <strong>{{ data.count }}</strong>
            </p>
            <button
              class="p-0 btn btn-lg text-danger"
              @click="increaseTicketTypeCount(data, 'add')"
            >
              <i class="bi bi-plus-circle"></i>
            </button>
          </div>
        </div>
      </div>
      <div class="row mb-5">
        <div class="col">
          <div class="d-flex justify-content-center">
            <button class="px-5 btn btn-danger" @click="checkForTicket">
              <p class="m-0 px-5">NEXT</p>
            </button>
          </div>
        </div>
      </div>
    </div>

    <div v-else>
      <div class="row justify-content-center">
        <div class="col col-md-6">
          <div class="d-flex">
            <div>
              <p>
                <small>{{ ticketString }}</small>
              </p>
            </div>
            <div class="ms-auto">
              <button class="p-0 btn btn-danger" @click="changeTicket">
                <i class="bi bi-chevron-right"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div
        class="
          mb-2
          row
          border-bottom border-danger border-3
          justify-content-center
        "
      >
        <div class="mt-5 col col-md-6">
          <div class="d-flex flex-column">
            <div>
              <p class="h6"><strong>Review</strong></p>
            </div>
          </div>
        </div>
      </div>

      <div class="row justify-content-center">
        <div class="col col-md-6">
          <div class="d-flex flex-row">
            <div>
              <p>
                <small>{{ ticketString }}</small>
              </p>
            </div>
            <div class="ms-auto d-flex">
              <p>
                <small>{{ priceDetails }} = &#2547;{{ totalPrice }}</small>
              </p>
            </div>
          </div>
          <hr />
        </div>
        <div class="row justify-content-center">
          <div class="col col-md-6">
            <div class="d-flex">
              <div>
                <p><strong>Total</strong></p>
              </div>
              <div class="ms-auto">
                <p>&#2547;{{ totalPrice }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Ticket",
  data() {
    return {
      ticket: {
        Adult: { price: 350, count: 0 },
        Child: { price: 200, count: 0 },
        Senior: { price: 150, count: 0 },
      },
      bookingData: {},
      ticketString: "",
      priceDetails: "",
      totalPrice: 0,
    };
  },
  mounted() {
    this.checkForTicket();
  },
  methods: {
    increaseTicketTypeCount(ticket, sign) {
      if (
        this.ticket.Adult.count +
          this.ticket.Child.count +
          this.ticket.Senior.count <
        5
      ) {
        if (sign === "add") ticket.count += 1;
      }
      if (sign === "remove" && ticket.count > 0) ticket.count -= 1;
    },
    getReview() {
      this.ticketString = "";
      this.priceDetails = "";
      this.totalPrice = 0;
      for (const ticketType in this.bookingData.ticket) {
        if (Object.hasOwnProperty.call(this.bookingData.ticket, ticketType)) {
          const element = this.bookingData.ticket[ticketType];
          if (element.count > 0) {
            this.ticketString += element.count + " " + ticketType + ", ";
            this.priceDetails +=
              element.count + " x " + "\u09F3" + element.price + " + ";
            this.totalPrice += element.count * element.price;
          }
        }
      }
      this.ticketString = this.ticketString.slice(
        0,
        this.ticketString.length - 2
      );
      this.priceDetails = this.priceDetails.slice(
        0,
        this.priceDetails.length - 3
      );
    },
    checkForTicket(event) {
      if (localStorage.getItem("bookingData")) {
        this.bookingData = JSON.parse(localStorage.getItem("bookingData"));
      }

      if (this.bookingData.ticket) {
        this.getReview();
      } else if (
        this.ticket.Adult.count +
        this.ticket.Child.count +
        this.ticket.Senior.count
      ) {
        this.bookingData.ticket = this.ticket;
        this.bookingData.totalPrice = 0;
        this.bookingData.totalPrice +=
          this.ticket.Adult.count * this.ticket.Adult.price +
          this.ticket.Child.count * this.ticket.Child.price +
          this.ticket.Senior.count * this.ticket.Senior.price;
        this.$store.commit("setTicket", this.bookingData);
        this.getReview();
      }
    },
    changeTicket(event) {
      if (
        this.bookingData.hasOwnProperty("ticket") &&
        this.bookingData.hasOwnProperty("totalPrice")
      ) {
        delete this.bookingData.ticket;
        delete this.bookingData.totalPrice;
        this.$store.commit("setTicket", this.bookingData);
      }
    },
  },
};
</script>
    <!-- <div class="mb-2 row border-bottom border-danger border-3">
      <div class="mt-5 col" style="margin-left: 25rem; margin-right: 25rem">
        <div class="d-flex flex-column">
          <div>
            <p class="mb-0 h6"><strong>Number of Ticket(s)</strong></p>
            <p class="mb-2">
              <small>You can reserve upto 5 seats per booking</small>
            </p>
          </div>
        </div>
      </div>
    </div>
    <div v-if="!bookingData.ticket">
      <div class="row">
        <div class="my-3 col" style="margin-left: 25rem; margin-right: 25rem">
          <div
            class="d-flex flex-row"
            v-for="(data, ticketType) in ticket"
            :key="ticketType"
          >
            <div>
              <p class="mb-0 h6">
                {{ ticketType }}
              </p>
              <p class="text-muted lh-1">
                <small>&#2547;{{ data.price }}</small>
              </p>
            </div>
            <div class="ms-auto">
              <div class="d-flex flex-column">
                <div class="d-flex flex-row">
                  <button
                    class="p-0 btn btn-lg text-danger"
                    @click="increaseTicketTypeCount(data, 'remove')"
                  >
                    <i class="bi bi-dash-circle"></i>
                  </button>
                  <p class="m-2 h6">
                    <strong>{{ data.count }}</strong>
                  </p>
                  <button
                    class="p-0 btn btn-lg text-danger"
                    @click="increaseTicketTypeCount(data, 'add')"
                  >
                    <i class="bi bi-plus-circle"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col" style="margin-left: 25rem; margin-right: 25rem">
          <div class="d-flex justify-content-center">
            <button class="px-5 btn btn-danger" @click="checkForTicket">
              <p class="m-0 px-5">NEXT</p>
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <div class="row">
        <div class="col" style="margin-left: 25rem; margin-right: 25rem">
          <div class="d-flex">
            <div>
              <p>
                <small>{{ ticketString }}</small>
              </p>
            </div>
            <div class="ms-auto">
              <button class="p-0 btn btn-danger" @click="changeTicket">
                <i class="bi bi-chevron-right"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="mb-2 row border-bottom border-danger border-3">
        <div class="mt-5 col" style="margin-left: 25rem; margin-right: 25rem">
          <div class="d-flex flex-column">
            <div>
              <p class="h6"><strong>Review</strong></p>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col" style="margin-left: 25rem; margin-right: 25rem">
          <div class="d-flex flex-row">
            <div>
              <p>
                <small>{{ ticketString }}</small>
              </p>
            </div>
            <div class="ms-auto d-flex">
              <p>
                <small>{{ priceDetails }} = &#2547;{{ totalPrice }}</small>
              </p>
            </div>
          </div>
          <hr />
        </div>
        <div class="row">
          <div class="col" style="margin-left: 25rem; margin-right: 25rem">
            <div class="d-flex">
              <div>
                <p><strong>Total</strong></p>
              </div>
              <div class="ms-auto">
                <p>&#2547;{{ totalPrice }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div> -->