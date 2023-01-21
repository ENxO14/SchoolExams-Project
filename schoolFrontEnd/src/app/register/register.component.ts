import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  name: string = '';
  lname: string= '';
  email: string= '';
  password: string= '';
  errorMessage: string= '';
  successMessage: string= '';
  data: any;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get('https://5000-enxo14-schoolexamsproje-ztr8nn7713j.ws-eu83.gitpod.io/register')
      .subscribe(
        (response) => {
          this.data = response;
          console.log(this.data);
        },
        (error) => {
          console.log(error);
        }
      );
  }

  register() {
    this.http.post('/register', { name: this.name, lname: this.lname, email: this.email, password: this.password })
      .subscribe(
        (response) => {
          this.successMessage = "You have successfully registered!";
        },
        (error) => {
          this.errorMessage = error.error.message;
        }
      );
  }
}
