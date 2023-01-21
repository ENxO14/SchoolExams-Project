import { UserService } from '../user.service';
import { User } from '../user';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import {Location} from '@angular/common'

@Component({
  selector: 'app-create-verif-sci',
  templateUrl: './create-verif-sci.component.html',
  styleUrls: ['./create-verif-sci.component.css']
})
export class CreateVerifSciComponent implements OnInit{
  user: User = new User();
  submitted = false;

  constructor(private userService: UserService,
    private router: Router,private location: Location ) { }

  ngOnInit() {
  }

  newUser(): void {
    this.submitted = false;
    this.user = new User();
  }

  save() {
    this.userService
    .createverifSci(this.user).subscribe(data => {
      console.log(data)
      this.user = new User();
      this.gotoList();
    }, 
    error => console.log(error));
  }

  onSubmit() {
    this.submitted = true;
    this.save();    
  }

  gotoList() {
    this.router.navigate(['/verifSci']);
  }

  back() : void
  {
    this.location.back();
  }
}
