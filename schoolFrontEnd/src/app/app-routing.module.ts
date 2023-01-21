import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { CreateUserComponent } from './create-user/create-user.component';
import { CreateVerifSciComponent } from './create-verif-sci/create-verif-sci.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { UpdateUserComponent } from './update-user/update-user.component';
import { UpdateVerifSciComponent } from './update-verif-sci/update-verif-sci.component';
import { UserListComponent } from './user-list/user-list.component';
import { VerifSciListComponent } from './verif-sci-list/verif-sci-list.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'users', component: UserListComponent },
  { path: 'add', component: CreateUserComponent },
  { path: 'update/:id', component: UpdateUserComponent },
  { path: 'verifSci', component: VerifSciListComponent },
  { path: 'addverifSci', component: CreateVerifSciComponent },
  { path: 'verifSciupdate/:id', component: UpdateVerifSciComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
