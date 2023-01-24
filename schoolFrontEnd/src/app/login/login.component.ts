import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {
  email: string = '';
  password: string = '';
  errorMessage: string = '';
  successMessage: string = '';
  obsLog: Observable<object> | undefined
  data: any = undefined!;

  constructor(private http: HttpClient, public router: Router) { }

  ngOnInit() {

  }

  /*login() {
    const data = { email: this.email, password: this.password };
    console.log("0");
    this.obsLog = this.http.post('https://5000-enxo14-schoolexamsproje-cpo672s3qv9.ws-eu83.gitpod.io/login', data)
    console.log("1");
    this.obsLog.subscribe(this.fati,(error) => {
      this.errorMessage = error.error.message;
  })
  }

  fati = (data: object) => {
    this.data = data;
    console.log(this.data);
    if (Object.keys(this.data).length === 0 || this.data.hasOwnProperty('error')) {
      this.errorMessage = "Error: Invalid email or password";
    } else {
      this.successMessage = "You have successfully logged!";
      localStorage.setItem('user', JSON.stringify(this.data));
      console.log("2.1");
      this.router.navigate(['/dashboard']);
    }
  }*/
  login() {
    const data = { email: this.email, password: this.password };
    console.log("0");
    this.http.post('https://5000-enxo14-schoolexamsproje-cpo672s3qv9.ws-eu83.gitpod.io/login', data).subscribe(
      data => {
        console.log(data);
        if (data.hasOwnProperty('error')) {
          this.errorMessage = "Error: Invalid Informations!!";
        } else {
          this.successMessage = "You have successfully Registerd!";
          localStorage.setItem('user', JSON.stringify(data));
          this.router.navigate(['/dashboard']);
        }
      },
      error => {
        console.log(error);
        this.errorMessage = "Error: Invalid Informations!!";
  })
  }

}

