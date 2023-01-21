import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateVerifSciComponent } from './create-verif-sci.component';

describe('CreateVerifSciComponent', () => {
  let component: CreateVerifSciComponent;
  let fixture: ComponentFixture<CreateVerifSciComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateVerifSciComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreateVerifSciComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
